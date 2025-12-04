def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.strip())

    return file_list

def is_valid_pos(row, col, row_len, col_len):
    #keeps us within bounds of the board
    if row < 0 or col < 0 or row >= row_len or col >= col_len:
        return False
    return True

def count_adjacent_rolls(row, col, file_list):
    row_len = len(file_list)
    col_len = len(file_list[row])

    adjacent_rolls = 0

    if is_valid_pos(row - 1, col - 1, row_len, col_len):
        if file_list[row - 1][col - 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row - 1, col, row_len, col_len):
        if file_list[row - 1][col] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row - 1, col + 1, row_len, col_len):
        if file_list[row - 1][col + 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row, col - 1, row_len, col_len):
        if file_list[row][col - 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row, col + 1, row_len, col_len):
        if file_list[row][col + 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row + 1, col - 1, row_len, col_len):
        if file_list[row + 1][col - 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row + 1, col, row_len, col_len):
        if file_list[row + 1][col] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row + 1, col + 1, row_len, col_len):
        if file_list[row + 1][col + 1] == '@':
            adjacent_rolls += 1

    return adjacent_rolls

def roll_can_be_removed(row, col, file_list):
    
    #if its not a roll, we don't care
    if file_list[row][col] != '@':
        return False
    
    #if there are less than 4 adjacent rolls, we can remove it
    if count_adjacent_rolls(row, col, file_list) < 4:
        return True
    return False

def evaluate_board(file_list):
    rolls_to_remove_this_pass = 0
    change_made = False

    #look at each item on the board
    for row in range(0, len(file_list)):
        for col in range(0, len(file_list[row])):
            if roll_can_be_removed(row, col, file_list):
                file_list[row] = file_list[row][:col] + 'x' + file_list[row][col + 1:]
                change_made = True
                rolls_to_remove_this_pass += 1

    return [rolls_to_remove_this_pass, file_list, change_made]

def play_game(file_list):

    total_rolls_removed = 0
    check_board = True

    #run until no changes are made on any given pass
    while check_board:
        output = evaluate_board(file_list)
        total_rolls_removed += output[0]
        file_list = output[1]
        check_board = output[2]

    return total_rolls_removed

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))