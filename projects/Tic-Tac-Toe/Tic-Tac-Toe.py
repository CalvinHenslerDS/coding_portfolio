# Tic-Tac-Toe

import numpy as np
import random

def coin_flip():

    # Prompt an input from the user, which will be used to determine whether the user or the computer will move first
    heads_tails = input("Select Heads or Tails:")

    # Generate a random integer (1 or 2) to simulate the result of a coin flip
    flip_result = random.randint(1,2)

    # Initialize a boolean to track whether it is currently the user's or the computer's turn to play
    computer_move = None

    # Convert heads_tales to an integer (1 or 2) to compare to flip_result
    if heads_tails == "Heads":
        heads_tails = 1
    else:
        heads_tails = 2

    # Print the result of the coin flip
    if flip_result == 1:
        print("The coin landed on Heads.")
    else:
        print("The coin landed on Tails.")

    # Print who will play move
    if flip_result == heads_tails:
        computer_move = False
        print("You go first!")
    else:
        computer_move = True
        print("The computer goes first.")

    # Return computer_move for use in play_game
    return computer_move

def random_index_from_mask(board):

    # Generate a mask from the input board containing all items equal to zero
    mask = (board == 0)

    # Generate a tuple of 1D arrays that makeup the indices of the items in the mask
    candidate_indices = np.where(mask)
    
    # Randomly choose an index from candidate_indices
    random_index_in_candidates = np.random.choice(len(candidate_indices[0]))

    # Return a tuple that consists of the random_index_in-candidates-th term of each NumPy array in the candidate_indices tuple
    return tuple(index[random_index_in_candidates] for index in candidate_indices)

def make_move(board, computer_move):

    # If it is the computer's move, change a randomly-selected item in board from 0 to 1
    if computer_move == True:
        computer_move_coordinates = random_index_from_mask(board)
        board[computer_move_coordinates] = 1

    # Otherwise, prompt the user to input the row and column of an item in board that is currently equal to 0, and change it to 2
    else:
        player_move_coordinates = input("Select an empty square to place an 'O' in: (format: row#,column#)")
        player_move_coordinates_int_list = list(map(int, player_move_coordinates.split(',')))

        # Initialize a boolean to facilitate error handling if an invalid input is given
        valid = False

        # Initialize a while loop to iterate until the input is valid
        while valid == False:
            
            # If the input corresponds to coordinates of an item in board that is equal to 0, toggle valid to break from the while loop
            if board[player_move_coordinates_int_list[0]][player_move_coordinates_int_list[1]] == 0:
                valid = True

            # If the input does not correspond to coordinates of an item in board that is equal to 0, prompt the user for a valid input and repeat the validation check
            else:
                print("That input is invalid.")
                player_move_coordinates = input("Select an empty square to place an 'O' in: (format: row#,column#)")
                player_move_coordinates_int_list = list(map(int, player_move_coordinates.split(',')))

        # Update board with the user's valid input
        board[player_move_coordinates_int_list[0], player_move_coordinates_int_list[1]] = 2
    
    # Toggling computer_move to ensure the opposite party moves when make_move is called again
    computer_move = not computer_move

    # Return the current board state and computer_move
    return board, computer_move

def win_check(board):

    # Initialize booleans to track whether the computer or the user has satisfied a win condition
    computer_winner = False
    challenger_winner = False

    # Initialize empty lists to store the lengths of the sets of the rows and columns of board
    set_lengths_rows = []
    set_lengths_columns = []

    # Calculate the length of the set of the diagonal and antidiagonal of board
    set_length_diag = len(set(np.diag(board)))
    set_length_antidiag = len(set(np.diag(np.fliplr(board))))

    # Calculate the sum of the diagonal and antidiagonal of board
    sum_diag = sum(np.diag(board))
    sum_antidiag = sum(np.diag(np.fliplr(board)))
    
    
    for i in board:

        # Append the length of the set of each row to set_lengths_rows
        set_lengths_rows.append(len(set(i)))

        # Create an array comprised of the sums of the items in the rows of board
        sum_rows = np.sum(board, axis=1)

        # Create an array comprised of the sums of the items in the columns of the board
        sum_columns = np.sum(board, axis=0)

    # Append the length of the set of each column to set_lengths_columns
    for i in board.T:
         set_lengths_columns.append(len(set(i)))

    # Convert sum_rows and sum_columns to lists
    sum_rows_list = sum_rows.tolist()
    sum_columns_list = sum_columns.tolist()



    sum_columns_list = sum_columns.tolist()

    print(set_lengths_columns)
    print(sum_columns)
    print(sum_columns_list)

    if set_length_diag == 1:
        if sum_diag == 3:
            computer_winner = True
            print(board, "The computer won along the diagonal")
            return computer_winner, challenger_winner
        elif sum_diag == 6:
            challenger_winner = True
            print(board, "The challenger won along the diagonal")
            return computer_winner, challenger_winner
        else:
            pass
    
    if set_length_antidiag == 1:
        if sum_antidiag == 3:
            computer_winner = True
            print(board, "The computer won along the antidiagonal")
            return computer_winner, challenger_winner
        elif sum_antidiag == 6:
            challenger_winner = True
            print(board, "The challenger won along the antidiagonal")
            return computer_winner, challenger_winner
        else:
            pass

    for i in set_lengths_columns:
        if set_lengths_columns[i] == 1 and sum_columns_list[i] == 3:
            computer_winner = True
            print(board, "The computer won along column %i" % i)
            return computer_winner, challenger_winner
        elif set_lengths_columns[i] == 1 and sum_columns_list[i] == 6:
            challenger_winner = True
            print(board, "The challenger won along column %i" % i)
            return computer_winner, challenger_winner
        else:
            continue

    for i in set_lengths_rows:
        if set_lengths_rows[i] == 1 and sum_rows_list[i] == 3:
            computer_winner = True
            print(board, "The computer won along column %i" % i)
            return computer_winner, challenger_winner
        elif set_lengths_rows[i] == 1 and sum_rows_list[i] == 6:
            challenger_winner = True
            print(board, "The challenger won along column %i" % i)
            return computer_winner, challenger_winner
        else:
            return computer_winner, challenger_winner

def play_game():
    board = np.zeros((3,3))
    computer_move = coin_flip()
    
    for i in range(10):
        print(board)
        board, computer_move = make_move(board, computer_move)
        computer_winner, challenger_winner = win_check(board)
        if (computer_winner or challenger_winner) == True:
            return computer_winner, challenger_winner, board
        else:
            continue

play_game()

'''
    if computer_turn == True:

        if len(candidate_positions) > 0:
            random_candidate_position = np.random.choice(candidate_positions)
'''


'''
    if len(candidate_positions) > 0:
        random_candidate_position = np.random.choice(candidate_positions)
'''        



'''
def play_tic_tac_toe():

    computer_first = coin_flip()

    if computer_first == True:
        


play_tic_tac_toe()
'''