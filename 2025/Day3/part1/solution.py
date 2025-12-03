def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.split("\n")[0])

    return file_list

def evaluate_line(line):
    left = 0
    left_ix = 0
    right = int(line[-1])

    for i in range(0, len(line) - 1):
        if int(line[i]) > left:
            left = int(line[i])
            left_ix = i
    
    for i in range(left_ix + 1, len(line)):
        if int(line[i]) > right:
            right = int(line[i])

    return int(str(left) + str(right))

def play_game(file_list):

    total_joltage = 0

    for i in range(0, len(file_list)):
        total_joltage += evaluate_line(file_list[i])
    
    return total_joltage        

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))