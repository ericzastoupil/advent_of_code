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
            range_list.append(i)
        else:
            ID_list.append(int(i))
    
    return range_list, ID_list

def play_game(file_list):

    fresh_IDs = 0
    
    range_list, ID_list = separate_lists(file_list)

    for ID in ID_list:
        for r in range_list:
            if ID >= int(r.split('-')[0]) and ID <= int(r.split('-')[1]):
                fresh_IDs += 1
                break
    
    return fresh_IDs

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))