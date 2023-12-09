def get_input(lines):
    directions = lines[0].strip()
    temp_dict = {}

    for line in lines[2:]:
        full_line = line.split(' = ')
        directions_tuple = (full_line[1].strip()[1:4], full_line[1].strip()[6:9])
        temp_dict[full_line[0]] = directions_tuple

    return directions, temp_dict

def play_game(directions, map_dict):

    at_end = False
    dir_idx = 0
    location = 'AAA'
    count = 0

    while not at_end:
        if dir_idx == len(directions):
            dir_idx = 0
            continue
        if location == 'ZZZ':
            return count
        else:
            if directions[dir_idx] == 'L':
                location = map_dict[location][0]
            else:
                location = map_dict[location][1]
        
        count += 1
        dir_idx += 1

        if location == 'ZZZ':
            return count                 

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    directions, map_dict = get_input(lines)

    print(play_game(directions, map_dict))
