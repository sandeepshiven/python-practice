#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:34:11 2019

@author: sandeep
"""

turns = [0,1,2,3,4,5,6,7,8]
print(turns[::4])
print(turns[2:7:2])
print(turns[2::3])

'''
if initial_player_value[0] == 'X':
        if (['X','X','X'] in check[:3]) or (['X','X','X'] in check[3:7]) or (['X','X','X'] in check[7:]):
            return "Player X wins"
        elif (['X','X','X'] in check[::3]) or (['X','X','X'] in check[1::3]) or (['X','X','X'] in check[2::3]):
            return "Player X wins"
        elif (['X','X','X'] in check[::4]) or (['X','X','X'] in check[2::2]):
            return "Player X wins"
        else:
            return "_"
        
    elif initial_player_value[0] == 'O':
        if (['O','O','O'] in check[:3]) or (['O','O','O'] in check[3:7]) or (['O','O','O'] in check[7:]):
            return "Player O wins"
        elif (['O','O','O'] in check[::3]) or (['O','O','O'] in check[1::3]) or (['O','O','O'] in check[2::3]):
            return "Player O wins"
        elif (['O','O','O'] in check[::4]) or (['O','O','O'] in check[2::2]):
            return "Player O wins"
        else:
            return "_"
        
    elif initial_player_value[1] == 'O':
        if (['O','O','O'] in check[:3]) or (['O','O','O'] in check[3:7]) or (['O','O','O'] in check[7:]):
            return "Player O wins"
        elif (['O','O','O'] in check[::3]) or (['O','O','O'] in check[1::3]) or (['O','O','O'] in check[2::3]):
            return "Player O wins"
        elif (['O','O','O'] in check[::4]) or (['O','O','O'] in check[2::2]):
            return "Player O wins"
        else:
            return "_"
            
            
'''