#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:32:02 2019

@author: sandeep
"""

class Node:
    def __init__(self,data):
        self.data =data
        self.next= None
        
head = Node(3)
nodeB = Node (8)
nodeC = Node(4)
nodeD = Node(6)
nodeE = Node(7)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE  

def main():
    print(f"This linked list contains {count_nodes(head)} nodes")

def count_nodes(current):
    count = 1
    while current.next != None:
        current = current.next
        count += 1
    return count
main()
    