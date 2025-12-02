def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.split("\n")[0])

    return file_list

def find_new_pos(pos, dir, num):
    if dir == 'L':
        return (pos - num) % 100
    elif dir == 'R':
        return (pos + num) % 100

def play_game(file_list):
    num_zeroes = 0
    pos = 50

    for i in range(0, len(file_list)):
        pos = find_new_pos(pos, file_list[i][0], int(file_list[i][1:]))

        if pos == 0:
            num_zeroes += 1
    
    return num_zeroes        

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))