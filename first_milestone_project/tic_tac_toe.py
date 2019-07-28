#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:11:38 2019

@author: sandeep
"""

from os import name,system
from time import sleep
from random import randint



def game_board(turns):
    print(turns[6],"|",turns[7],"|",turns[8])
    print("--|---|---")
    print(turns[3],"|",turns[4],"|",turns[5])
    print("--|---|---")
    print(turns[0],"|",turns[1],"|",turns[2])
    
    

def check_input(player1,player2):
    if (player1 == 'X' or player1 == 'O') and (player2 == 'X' or player2 == 'O'):
        return True
    else:
        print("Please choose between X and O")
        global initial_player_value
        initial_player_value = take_input()
        return False





    
def take_input():
    player1 = input("Do you want 'X' or 'O'?\n")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)







def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
        
        
        
        
def player_turn(initial_player_value0,initial_player_value1):
    clear()
    global turns
    game_board(turns)
    print(f"Player {initial_player_value0} turn")
    print("Enter position")
    player1_input =input()
    turns.pop(int(player1_input)-1)
    turns.insert(int(player1_input)-1,initial_player_value0)
    clear()
    game_board(turns)
    
    print(f"Player {initial_player_value1} turn")
    print("Enter position")
    player2_input = input()
    turns.pop(int(player2_input)-1)
    turns.insert(int(player2_input)-1,initial_player_value1)
    clear()
    game_board(turns)
    
    
    
def win_check(check,initial_player_value3,initial_player_value4):
    
   # print(check)
    
    global game_status
    if initial_player_value3 == 'X':
        if ((['X','X','X'] == check[:3]) or (['X','X','X'] == check[3:6]) or (['X','X','X'] == check[6:])):
            game_status = "Player X wins"
        elif ((['X','X','X'] == check[::3]) or (['X','X','X'] == check[1::3]) or (['X','X','X'] == check[2::3])):
            game_status = "Player X wins"
        elif ((['X','X','X'] == check[::4]) or (['X','X','X'] == check[2:7:2])):
            game_status = "Player X wins"
        else:
            game_status = "_"
        
    else:
        if ((['O','O','O'] == check[:3]) or (['O','O','O'] == check[3:6]) or (['O','O','O'] == check[6:])):
            game_status = "Player O wins"
        elif ((['O','O','O'] == check[::3]) or (['O','O','O'] == check[1::3]) or (['O','O','O'] == check[2::3])):
            game_status = "Player O wins"
        elif ((['O','O','O'] == check[::4]) or (['O','O','O'] == check[2:7:2])):
            game_status = "Player O wins"
        else:
            game_status = "_"
        
    if initial_player_value4 == 'O':
        if ((['O','O','O'] == check[:3]) or (['O','O','O'] == check[3:6]) or (['O','O','O'] == check[6:])):
            game_status = "Player O wins"
        elif ((['O','O','O'] == check[::3]) or (['O','O','O'] == check[1::3]) or (['O','O','O'] == check[2::3])):
            game_status = "Player O wins"
        elif ((['O','O','O'] == check[::4]) or (['O','O','O'] == check[2:7:2])):
            game_status = "Player O wins"
        else:
            game_status = "_"
        
    else :
        if ((['X','X','X'] == check[:3]) or (['X','X','X'] == check[3:6]) or (['X','X','X'] == check[6:])):
            game_status = "Player X wins"
        elif ((['X','X','X'] == check[::3]) or (['X','X','X'] == check[1::3]) or (['X','X','X'] == check[2::3])):
            game_status = "Player X wins"
        elif ((['X','X','X'] == check[::4]) or (['X','X','X'] == check[2:7:2])):
            game_status = "Player X wins"
        else:
            game_status = "_"
    draw_check = ''.join(str(x) for x in check)
    print(draw_check)
    #sleep(5)
    if draw_check.isalpha():
        game_status ="Game draws"
    
    else:
        game_status= "_"
    
        
    
    
    
    
    
    
    
#def welcome():
print("Welcome to the tic tac toe game\n")
initial_player_value = take_input()
check = check_input(initial_player_value[0],initial_player_value[1])
while check is False:
    check = check_input(initial_player_value[0],initial_player_value[1])
print(f"Player 1 is {initial_player_value[0]} and Player 2 is {initial_player_value[1]}\nLet's start the game" )

turns = [1,2,3,4,5,6,7,8,9]
sleep(2)
clear()
game_board(turns)
game_status = '_'
decide_first = randint(1,2)
replay = 'yes'



while replay == "yes":
    #global game_status
    if decide_first == 1:
        player_turn(initial_player_value[0],initial_player_value[1])
        game_board(turns)
        win_check(turns,initial_player_value[0],initial_player_value[1])
    else:
        player_turn(initial_player_value[1],initial_player_value[0])
        game_board(turns)
        win_check(turns,initial_player_value[0],initial_player_value[1])
    
    #win_check(turns,tuple(initial_player_value))    
    if game_status != '_':
        print(game_status)
        replay = input("Do you want to play again?\n")
        turns = [1,2,3,4,5,6,7,8,9]
    












