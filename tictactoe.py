# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:55:03 2018

@author: James
"""
import random

def tictactoe():
    board = str(' _ _ _ _ _ _ _ _ _\n|     |     |     |\n|     |     |     |\n|_ _ _|_ _ _|_ _ _|\n|     |     |     |\n|     |     |     |\n|_ _ _|_ _ _|_ _ _|\n|     |     |     |\n|     |     |     |\n|_ _ _|_ _ _|_ _ _|')
    board_list = list(board)
    positions = board
    piece_positions = [42, 48, 54, 102, 108, 114, 162, 168, 174]
    positions_list = list(positions)
    symbols = ['X','O']
    
    for i in piece_positions:
        positions_list[i] = str(piece_positions.index(i)+1)

    positions_list = "".join(positions_list)

    #piece positions at 42, 48, 54, 102, 108, 114, 162, 168, 174
    print('---------------------------------------------------------')
    user1 = input('Please enter player 1 name: ')
    print('---------------------------------------------------------')
    user2 = input('Please enter player 2 name: ')
    print('---------------------------------------------------------')
    print('Welcome {} and {}. Please enjoy your game and remember, no cheating!'.format(user1,user2))
    print('---------------------------------------------------------')
    players = [user1,user2]

    print('--------------------- STARTING GAME ---------------------')

    randplayers = players
    random.shuffle(randplayers)
    starting_player = randplayers[0]

    other_player = randplayers[1]
    
    print('{} has randomly been selected to start first!'.format(starting_player))
    print('---------------------------------------------------------')
    
    player1symbol = None
    
    while player1symbol not in symbols:
        
        player1symbol = input('{} which symbol would you like to use? Please type in X or O: '.format(starting_player))
        if player1symbol not in symbols:
            print('---------------------------------------------------------')
            print('Error! Please enter a valid piece symbol! (X or O)')
            print('---------------------------------------------------------')
        
        else:
            break
   
    if player1symbol == 'X':
        player2symbol = 'O'
    else:
        player2symbol = 'X'
    print('---------------------------------------------------------')
    print('{} is using the {} symbol, {} is using the {} symbol.'.format(starting_player, player1symbol, other_player, player2symbol))
    print('---------------------------------------------------------')
    print('This is the board layout, When taking your turn, enter the number corresponding to the region you would like to place your piece in.\n{}'.format(positions_list))
    print('---------------------------------------------------------')
            
    turns = [starting_player, other_player]*5
    pieces = [player1symbol, player2symbol]*5
    winning_conditions = [[42, 48, 54], [102, 108, 114], [162, 168, 174], [42, 102, 162], [48, 108, 168], [54, 114, 174], [42, 108, 174], [54, 108, 162]]
    wcoords = []
    turn = 0
    badturn = []
    
    game_active = True    
    for n in range(0,9):
 
        #while game_active is True:
        # CHECK IF GFAME HAS ENDED..
        
        while turn not in range(1,10):
        
            turn = int(input('{} please enter the region which you would like to place your piece in: '.format(turns[n])))
            
            if turn in badturn:
                print('---------------------------------------------------------')
                print('Error! That move has already been made!')
                print('---------------------------------------------------------')
                turn = 0
            else:
                
                if not 1<turn<10:
                    print('---------------------------------------------------------')
                    print('Error! Please enter a valid position (1-9)')
                    print('---------------------------------------------------------')
                    continue
        else:
            
            boardpos = piece_positions[turn-1]
            board_list[boardpos] = pieces[n]
            updatedboard = "".join(board_list)
            badturn.append(turn)
            turn = 0
            
            print('---------------------------------------------------------')
            print('Updating game board...\n---------------------------------------------------------\n{}'.format(updatedboard))
            print('---------------------------------------------------------')
            
            if n >=5: #Only check for a winner if past the fifth turn
            # Check for a winner
                for i in range(0,7):  
                    
                    wcoords = winning_conditions[i]
              
                    if updatedboard[wcoords[0]] == pieces[n]:              
                        if updatedboard[wcoords[1]] == pieces[n]:                    
                            if updatedboard[wcoords[2]] == pieces[n]:
                                
                                print('Congratulations {} has won the game!'.format(turns[n]))
                                game_active = False
                                
                                restart = input('Would you like to play again? Please enter \'y\' or \'n\': ')
                                if restart == 'y':
                                    tictactoe()
                                break                    
                    else:                
                        continue
            
            
        if game_active is False: 
            break
        if game_active is True and n == 8:
               
            print('The game has resulted in a tie!')
            restart = input('Would you like to play again? Please enter \'y\' or \'n\': ')
            if restart == 'y':
                tictactoe()
                
            break
tictactoe()
            
                         