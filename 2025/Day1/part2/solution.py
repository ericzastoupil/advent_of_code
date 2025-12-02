def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.split("\n")[0])

    return file_list

def find_passes(pos, dir, num):
    passes = 0

    if dir == "R":
        while pos + num > 100:
            num -= 100
            passes += 1             
    else:
        if pos == 0:
            passes -= 1
        while pos - num < 0:
            num -= 100
            passes += 1
    
    return passes

    
def find_new_pos(pos, dir, num):
    
    passes = find_passes(pos, dir, num)
    
    if dir == 'L':
        new_pos = (pos - num) % 100
    elif dir == 'R':
        new_pos = (pos + num) % 100
    
    return new_pos, passes

def play_game(file_list):
    num_zeroes = 0
    num_passes = 0
    pos = 50

    for i in range(0, len(file_list)):
        pos, passes = find_new_pos(pos, file_list[i][0], int(file_list[i][1:]))

        if pos == 0:
            num_zeroes += 1

        num_passes += passes
    
    return num_zeroes + num_passes        

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))