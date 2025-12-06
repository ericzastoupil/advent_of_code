def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.split())

    return file_list

def convert_to_ceph(reg_list):
    ceph_list = ['0' for _ in range(0, len(reg_list))]
    
    for num in range(0, len(reg_list)):
        if num < len(reg_list):
            ceph_list[num] += reg_list[num]
        else:
            ceph_list[num] += '0'
    
    print(ceph_list)

    return ceph_list


def evaluate_row(row):
    ceph_list = convert_to_ceph(row[:-1])
    ceph_list.append(row[-1])

    final = 0
    if ceph_list[-1] == '*':
        final = 1
        for elem in ceph_list[:-1]:
            final *= int(elem)
    else:
        for elem in ceph_list[:-1]:  
            final += int(elem)

    return final


def play_game(file_list):

    total_solution = 0

    transposed_list = [list(row) for row in zip(*file_list)]

    for row in transposed_list:
        total_solution += evaluate_row(row)
    
    return total_solution

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("test_input.txt")))
    #print("Solution: ", play_game(get_input("input.txt")))