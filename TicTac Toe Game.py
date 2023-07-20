#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def display_board(board):
   
    
    print('  |   |')
    print('' + board[7] +' | ' + board[8] + ' | '+ board[9])
    print('  |   |')
    print('----------')
    print('  |   |')
    print('' + board[4] + ' | ' + board[5] + ' | '+ board[6])
    print('  |   |')
    print('----------')
    print('  |   |')
    print('' + board[1] +' | '+ board[2] + ' | ' + board[3])
    print('  |   |')


# In[ ]:


test_board=['*','X','O','X','X','O','O','X','X','O']
display_board(test_board)


# In[ ]:


def player_input():
    marker=''
    
    while not (marker=='X' or marker == 'O'):
        marker=input('Player 1: Do you want to be X or O?').upper()
        
    if marker=='X':
        return('X','O')
    else:
        return('O','X')


# In[ ]:


player_input()


# In[ ]:


def place_marker(board,marker, position):
    board[position]= marker


# In[ ]:


place_marker(test_board,'&',9)
display_board(test_board)


# In[ ]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))


# In[ ]:


win_check(test_board,'X')


# In[ ]:


import random 

def choose_first():
    if random.randint(0,1)== 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[ ]:


def space_check(board,position):
    return board[position]== ' '


# In[ ]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    


# In[ ]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[ ]:


def replay():
    return input('Do you want to play again? Enter Yes or No')


# In[ ]:


print('Welcome to TIC TAC TOE!!')

while True:
    theboard=[' ']*10
    player1_marker,player2_marker = player_input()
    turn=choose_first()
    print(turn + ' will go first.')
    
    play_game= input('Are you ready to play? Enter Yes or No')
    
    if play_game.lower()[0]== 'y':
        game_on = True
    else:
        game_on=False
    
    while game_on:
        if turn== 'Player 1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print('Congratulations! Player 1 have won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Congratulations! Player 2 have won the game!')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break


# In[ ]:





# In[ ]:





# In[ ]:




