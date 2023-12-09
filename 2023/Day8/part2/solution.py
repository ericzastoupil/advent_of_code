def get_input(lines):
    directions = lines[0].strip()
    temp_dict = {}
    starting_nodes = []

    for line in lines[2:]:
        full_line = line.split(' = ')
        directions_tuple = (full_line[1].strip()[1:4], full_line[1].strip()[6:9])
        temp_dict[full_line[0]] = directions_tuple
        if full_line[0][2] == 'A':
            starting_nodes.append(full_line[0])

    return starting_nodes, directions, temp_dict

def iterate_until_complete(node, directions):
    at_end = False
    dir_idx = 0
    location = node
    count = 0

    while not at_end:
        if dir_idx == len(directions):
            dir_idx = 0
            continue
        if location[2] == 'Z':
            return count
        else:
            if directions[dir_idx] == 'L':
                location = map_dict[location][0]
            else:
                location = map_dict[location][1]
        
        count += 1
        dir_idx += 1

def play_game(nodes, directions):

    freqs = []

    for i in range(len(nodes)):
        freqs.append(iterate_until_complete(nodes[i], directions))
    
    return freqs

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    starting_nodes, directions, map_dict = get_input(lines)

    frequencies = play_game(starting_nodes, directions)
    print(frequencies) #lcm of each of these
