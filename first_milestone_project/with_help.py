#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:00:45 2019

@author: sandeep
"""
from os import system,name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



def display_board(board):
    
    print(board[7],"|",board[8], "|",board[9])
    print("--|---|---") 
    print(board[4],"|",board[5], "|",board[6])
    print("--|---|---")
    print(board[1],"|",board[2], "|",board[3])
    
    
def player_input():
    
    marker = ''
    while not (marker == "X" or marker == "O"):
        print("Player 1 do you want X or O?")
        marker = input().upper()
    if marker == "X":
        return("X","O")
    else:
        return("O","X")
        
        
def place_marker(board, marker, position):
    board.pop(position)
    board.insert(position,marker)
    
    
    
    
def win_check(board, mark):
    
    return ((board[1]==mark and board[2] == mark and board[3]== mark)or
    (board[4]==mark and board[5] == mark and board[6]== mark)or
    (board[7]==mark and board[8] == mark and board[9]== mark)or
    (board[1]==mark and board[4] == mark and board[7]== mark)or
    (board[2]==mark and board[5] == mark and board[8]== mark)or
    (board[3]==mark and board[6] == mark and board[9]== mark)or  
    (board[7]==mark and board[5] == mark and board[3]== mark)or
    (board[1]==mark and board[5] == mark and board[9]== mark))
    
    
    
    
import random

def choose_first():
    
    return("Player {} ".format(random.randint(1,2)))
    
    
    
def space_check(board, position):
    
    return not(board[position] =="X"or board[position] =="O")



def full_board_check(board):
    x = ''
    for y in board[1:]:
        x = x+y
    return(x.isalpha())
    
    
    
    
    
def player_choice(board):
    position = int(input("Enter the position    "))
    clear()
    if space_check(board,position):
        return position
    
    
def replay():
    again = input("Do you want to play again?   ")
    if again == 'yes':
        return True
    return False



print('Welcome to Tic Tac Toe!')

while True:
    board = ['_']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first")
    
    play_game = input("Are you ready to play? Enter yes or no\n")
    
    if play_game.lower()[0]=="y":
        game_on = True
    else:
        game_on = False
    
    
    

    while game_on:
        if turn == "Player 1":
            #player 1 turn
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)
            
            
            if win_check(board,player1_marker):
                display_board(board)
                print("Congratulations! you have won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game draws")
                    break
                else:
                    turn = "Player 2"
            
        else:
                #player 2 turn
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker,position)
            
             
            if win_check(board,player2_marker):
                display_board(board)
                print("Congratulations! you have won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game draws")
                    break
                else:
                    turn = "Player 1"
            
        
        
       

    if not replay():
        break