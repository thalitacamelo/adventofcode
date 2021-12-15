import sys

with open('input.txt', 'r') as file:
    # Declaration of variable numbers(chosen numbers), readline () return a list of numbers in the first line of sample.txt.
    numbers = file.readline().strip().split(sep=',')
    # skiping the next line, which is empty
    file.readline()
    # Declaration of variable boards, a list of boards(5x5 grid of numbers, each row is a string separated by '\n').
    boards = file.read().split('\n\n')


## To easy acess of numbers and grid positions, dictionaries of 'number':(index_row,index_column) will be storaged in a list.
## Each dictionary will correpond to a board.
# Declaration of the list to hold the dictionaries. The dictionaries order will correspond to boards order in the boards list.
indexes = []
# Iteration over each board(each row is a string separated by '\n').
for board in boards:
    # Declaration of a dictionary to hold the key 'number' and a tuple with positions -> 'number':(index_row,index_column).
    board_index = {}
    # Initializing variable index_row.
    index_row = 0
    # Iteration over each row, board.split('\n') return a list of strings, each string has the numbers separated by space.
    for row in board.split('\n'):
        # Getting the numbers(keys of the board_index).
        keys = row.split()
        # Initializing variable index_col.
        index_col = 0
        # Iteration over each column.
        for k in keys:
            # Adding 'key':(index_row,index_column) to board_index.
            board_index[k] = (index_row,index_col)
            # moving to next column.
            index_col += 1
        # moving to next row.
        index_row += 1
    # Appending the dictionary with the numbers and indexes of the board to the list indexes.
    indexes.append(board_index)


## To keep record of how many numbers was marked in each row or colunm, a list will hold tuples of lists for each board -> row_columns = [(rows, columns),...,(rows, columns)].
# Initializing the row_columns_count list.
row_columns_count = []
# Iteration over boards
for i in range(len(boards)):
    # Creating row list. We know it is 5x5 grid of numbers.
    row = [0] * 5
    # Creating coliumn list. We know it is 5x5 grid of numbers.
    column = [0] * 5
    # Appending a tuple of rows and columns to row_columns list.
    row_columns_count.append((row,column))


winners = []
winners_index = []
# Iteration over numbers.
for number in numbers:
    # Iteration over boards.
    for i in range(len(boards)):
        if len(winners) == len(boards):
            break
        if i in winners_index:
            continue
        # Accessing the 'number':(index_row,index_column) dictionary
        board_dict = indexes[i]
        # Unpacking the row_count and col_count.
        row_count, col_count = row_columns_count[i]
        # Cheking if number is the board.
        if number in board_dict:
            row, column = board_dict[number]
            # Remove the marked number from the board.
            del board_dict[number]
            row_count[row] += 1
            col_count[column] += 1
            # Check completion of one row or column on a board
            if 5 in row_count or 5 in col_count:
                # If there is at least one complete row or column of marked numbers on a board, store the last number drawn and the winning board on winners. 
                winners.append((number, board_dict))
                # Keep record of winning board index on boards list
                winners_index.append(i)


last_number, last_winner_board = winners[-1]
sum = 0
for key in last_winner_board:
    # Sum of the of all unmarked numbers on the winner board
    sum += int(key)
score = int(last_number) * sum
print(score)