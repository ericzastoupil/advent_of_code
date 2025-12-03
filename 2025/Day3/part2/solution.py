def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.split("\n")[0])

    return file_list

def get_next_num(line):
    highest = 0
    idx_of_highest = 0
    
    for i in range(0, len(line)):
        if int(line[i]) > highest:
            highest = int(line[i])
            idx_of_highest = i
    
    return (str(highest), idx_of_highest)

def evaluate_line(line):
    start_ix_of_next_slice = 0
    longest_length = 12
    end_ix_of_next_slice = len(line) - longest_length + 1
    joltage_str = ''

    for i in range(0, longest_length):
        
        next_slice_to_evaluate = line[start_ix_of_next_slice:end_ix_of_next_slice]

        output = get_next_num(next_slice_to_evaluate)
        joltage_str += output[0]
        start_ix_of_next_slice += output[1] + 1
        end_ix_of_next_slice = len(line[start_ix_of_next_slice:]) - (longest_length - (i + 2)) + start_ix_of_next_slice

    return int(joltage_str)

def play_game(file_list):

    total_joltage = 0

    for i in range(0, len(file_list)):
        total_joltage += evaluate_line(file_list[i])
    
    return total_joltage        

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))