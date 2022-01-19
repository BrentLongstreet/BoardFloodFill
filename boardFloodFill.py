"""
Name: Brent Longstreet
Date: 03/08/2020
Project: FloodFill Board Game
"""

import random
import sys

def ShowBoard(displayBoard,player):
    #Displays Light up board
    displayBoard[player['row']][player['col']] = "@"
    for row in displayBoard:
        print(" ".join(row))
        
def PlacePlayer(board,player):
    #Places player on board
    while True:
        player['row'] = random.randint(0,len(board)-1)
        player['col'] = random.randint(0,len(board[0])-1)
        if board[player['row']][player['col']] == ".":
            board[player['row']][player['col']] = "@"
            break
            
    return board, player
        
def PlaceTorch(board,torch):
    #Places torch on board
    while True:
        torch['row'] = random.randint(0,len(board)-1)
        torch['col'] = random.randint(0,len(board[0])-1)
        if board[torch['row']][torch['col']] == ".":
            board[torch['row']][torch['col']] = "T"
            break
    return board, torch

def PlaceLantern(board,lantern):
    #Places lantern on board
    while True:
        lantern['row'] = random.randint(0,len(board)-1)
        lantern['col'] = random.randint(0,len(board[0])-1)
        if board[lantern['row']][lantern['col']] == ".":
            board[lantern['row']][lantern['col']] = "L"
            break
    return board, lantern

def MovePlayer(board,player):
    #User Movement
    while True:
        userInput = input("Which direction W/A/S/D? (Q) to Quit! ").upper()
        if userInput in ["W","A","S","D"]:
            break
        if userInput == "Q":
            input("Thanks for playing!")
            sys.exit(0)
    board[player['row']][player['col']] = "."
    #validation for not running into a wall
    if userInput == "W":
        if board[player['row']-1][player['col']] != "#":
            player['row'] -= 1
    elif userInput == "S":
         if board[player['row']+1][player['col']] != "#":
            player['row'] += 1
    elif userInput == "A":
         if board[player['row']][player['col']-1] != "#":
            player['col'] -= 1
    elif userInput == "D":
         if board[player['row']][player['col']+1] != "#":
            player['col'] += 1
    
    board[player['row']][player['col']] = "@"
    
    
    return board,player


def Floodfill(currRow, currCol, lightRadius, board, displayBoard, counter = 0):
    #Fuction for light
    if counter > lightRadius or board[currRow][currCol] == "#":
        return
    displayBoard[currRow][currCol] = board[currRow][currCol]
    counter += 1
    #Fills in around the player's current cords
    Floodfill(currRow+1,currCol,lightRadius,board,displayBoard, counter)
    Floodfill(currRow -1,currCol,lightRadius,board,displayBoard, counter)
    Floodfill(currRow,currCol + 1,lightRadius,board,displayBoard, counter)
    Floodfill(currRow,currCol - 1,lightRadius,board,displayBoard, counter)
    Floodfill(currRow+1,currCol - 1,lightRadius,board,displayBoard, counter)
    Floodfill(currRow+1,currCol + 1,lightRadius,board,displayBoard, counter)
    Floodfill(currRow-1,currCol + 1,lightRadius,board,displayBoard, counter)
    Floodfill(currRow-1,currCol - 1,lightRadius,board,displayBoard, counter)

    
def Main():
    # Non-visible game board
    board =[['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
            ['#','.','.','#','.','.','.','.','#','.','.','.','.','.','#'],
            ['#','.','.','#','.','.','.','.','#','.','.','.','.','.','#'],
            ['#','.','.','.','.','.','.','.','#','.','.','.','.','.','#'],
            ['#','.','.','.','.','.','.','.','#','.','.','.','.','.','#'],
            ['#','.','.','.','.','.','.','.','#','.','.','.','.','.','#'],
            ['#','.','.','.','.','.','.','.','#','.','.','.','.','.','#'],
            ['#','.','.','#','.','.','.','.','.','.','.','.','.','.','#'],
            ['#','.','.','#','.','.','.','.','.','.','.','.','.','.','#'],
            ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

    lightRadius = int(input("Enter a light radius: "))
    player = {}
    torch = {}
    lantern = {}
    PlacePlayer(board,player)
    PlaceTorch(board, torch)
    PlaceLantern(board, lantern)
    while True:
        #Visible game board
        displayBoard = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
        Floodfill(player['row'],player['col'],lightRadius,board,displayBoard)
        ShowBoard(displayBoard,player)
        MovePlayer(board,player)
        #torch item
        if board[player['row']][player['col']] == board[torch['row']][torch['col']]:
            print("YOU FOUND A TORCH!" + "\n")
            print("Light Radius = 4!")
            lightRadius = 4
        #Lantern item
        if board[player['row']][player['col']] == board[lantern['row']][lantern['col']]:
            print("YOU FOUND A LANTERN!" + "\n")
            print("Light Radius = 5!")
            lightRadius = 5
            
            
Main()
