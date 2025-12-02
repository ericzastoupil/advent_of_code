def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        line = file.readline()
        file_list = line.strip("\n").split(",")
        
    for i in range(0, len(file_list)):
        file_list[i] = (int(file_list[i].split('-')[0]), int(file_list[i].split('-')[1]))

    print(file_list)
    return file_list

def invalid_num(num):
    str_num = str(num)

    #if the first half of the number is the same as the back half
    if str_num[:len(str_num) // 2] == str_num[len(str_num) // 2:]:
        return num
    
    return 0

def sum_invalids_in_range(ID_range):
    sum_invalids_in_range = 0

    #run an independent check for each number in the range
    for num in range(ID_range[0], ID_range[1] + 1):
        sum_invalids_in_range += invalid_num(num)
    return sum_invalids_in_range

def play_game(file_list):

    sum_all_invalids = 0

    #check each range
    for range in file_list:
        sum_all_invalids += sum_invalids_in_range(range)

    return sum_all_invalids

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))