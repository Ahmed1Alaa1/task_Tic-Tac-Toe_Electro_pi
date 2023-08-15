#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ahmed alaa sobhy elbanby

# Create a function to print the game board:
   
def print_board(board):
   for row in board:
       print(" | ".join(row))
       print("-" * 9)
       
#Create a function to handle player moves:

def make_move(board, row, col, player_symbol):
   if board[row - 1][col - 1] == '':
       board[row - 1][col - 1] = player_symbol
       return True
   else:
       print("That square is already taken. Try again.")
       return False
   
#Create a function to check for a win:

def check_win(board, player_symbol):
   for i in range(3):
       if all(board[i][j] == player_symbol for j in range(3)) or           all(board[j][i] == player_symbol for j in range(3)):
           return True
   if all(board[i][i] == player_symbol for i in range(3)) or       all(board[i][2-i] == player_symbol for i in range(3)):
       return True
   return False

#Create a function to check for a tie:

def check_tie(board):
   return all(all(square != '' for square in row) for row in board)

#Create a main game loop:

def main():
   players = ['X', 'O']
   current_player = 0
   moves = 0
   board = [['', '', ''], ['', '', ''], ['', '', '']]

   while True:
       print_board(board)
       player_symbol = players[current_player]
       print(f"Player {player_symbol}, it's your turn.")
       
       while True:
           try:
               row = int(input("Enter row (1, 2, or 3): "))
               col = int(input("Enter column (1, 2, or 3): "))
               if 1 <= row <= 3 and 1 <= col <= 3:
                   if make_move(board, row, col, player_symbol):
                       moves += 1
                       break
               else:
                   print("Invalid input. Row and column must be between 1 and 3.")
           except ValueError:
               print("Invalid input. Please enter a valid number.")

       if check_win(board, player_symbol):
           print_board(board)
           print(f"Player {player_symbol} wins!")
           break
       elif check_tie(board):
           print_board(board)
           print("It's a tie!")
           break

       current_player = (current_player + 1) % 2

if __name__ == "__main__":
   main()


# In[ ]:




