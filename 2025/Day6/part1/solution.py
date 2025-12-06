def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.split())

    return file_list

def evaluate_row(row):
    final = 0
    if row[-1] == '*':
        final = 1
        for elem in row[:-1]:
            final *= int(elem)
    else:
        for elem in row[:-1]:  
            final += int(elem)

    return final


def play_game(file_list):

    total_solution = 0

    transposed_list = [list(row) for row in zip(*file_list)]

    for row in transposed_list:
        total_solution += evaluate_row(row)
    
    return total_solution

if __name__ == "__main__":
    #print("Solution: ", play_game(get_input("test_input.txt")))
    print("Solution: ", play_game(get_input("input.txt")))