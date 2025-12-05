def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.strip())

    return file_list

def separate_lists(file_list):
    range_list = []
    ID_list = []
    empty_found = False

    for i in file_list:
        if i == '':
            empty_found = True
            continue
        if not empty_found:
            range_list.append([int(i.split('-')[0]),int(i.split('-')[1])])
        else:
            ID_list.append(int(i))
    
    return range_list, ID_list

def consolidate_ranges(range_list):
    invalid_range = ['x', 'x']

    for i in range(0, len(range_list) - 1):
        for j in range(i + 1, len(range_list)):
            
            #if either is invalid, or no overlap
            if range_list[i] == invalid_range or range_list[j] == invalid_range or range_list[i][1] < range_list[j][0] - 1 or range_list[j][1] < range_list[i][0] - 1:
                continue

            #overlap on start of second only
            if range_list[i][0] <= range_list[j][0] and range_list[i][1] < range_list[j][1]:
                range_list[i][1] = range_list[j][1]
                range_list[j] = invalid_range
            
            #overlap on end of second only
            elif range_list[i][0] >= range_list[j][0] and range_list[i][1] > range_list[j][1]:
                range_list[i][0] = range_list[j][0]
                range_list[j] = invalid_range
            
            #first consumes second
            elif range_list[i][0] <= range_list[j][0]and range_list[i][1] >= range_list[j][1]:
                range_list[j] = invalid_range
            
            #first consumed by second
            elif range_list[i][0] >= range_list[j][0] and range_list[i][1] <= range_list[j][1]:
                range_list[i] = range_list[j]
                range_list[j] = invalid_range

    return range_list

def count_all_fresh_IDs(range_list):
    sum_of_all_ranges = 0

    for r in range_list:
        sum_of_all_ranges += r[1] - r[0] + 1

    return sum_of_all_ranges

def play_game(file_list):
    change_made = True
    range_list, _ = separate_lists(file_list)

    while change_made:
        range_list = consolidate_ranges(range_list)

        if ['x', 'x'] in range_list:
            range_list = [item for item in range_list if item != ['x', 'x']]
        else:
            change_made = False

    return count_all_fresh_IDs(range_list)


if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))