def get_input(lines):
    values= []
    count = 0
    for line in lines:
        if 'S' in line:
            start = [count, line.index('S')]
        values.append([*line.strip()])
        count += 1
    return start, values

def get_next(curr, prior):
    '''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    '''
    next_step = []
    if pipe_map[curr[0]][curr[1]] == '|':
        if prior[0] < curr[0]:
            next_step = [curr[0] + 1, curr[1]]
        else:
            next_step = [curr[0] - 1, curr[1]]
    elif pipe_map[curr[0]][curr[1]] == '-':
        if prior[1] < curr[1]:
            next_step = [curr[0], curr[1] + 1]
        else:
            next_step = [curr[0], curr[1] - 1]
    elif pipe_map[curr[0]][curr[1]] == 'L':
        if prior[0] < curr[0]:
            next_step = [curr[0], curr[1] + 1]
        else:
            next_step = [curr[0] - 1, curr[1]]
    elif pipe_map[curr[0]][curr[1]] == 'J':
        if prior[0] < curr[0]:
            next_step = [curr[0], curr[1] - 1]
        else:
            next_step = [curr[0] - 1, curr[1]]
    elif pipe_map[curr[0]][curr[1]] == '7':
        if prior[0] > curr[0]:
            next_step = [curr[0], curr[1] - 1]
        else:
            next_step = [curr[0] + 1, curr[1]]
    elif pipe_map[curr[0]][curr[1]] == 'F':
        if prior[0] > curr[0]:
            next_step = [curr[0], curr[1] + 1]
        else:
            next_step = [curr[0] + 1, curr[1]]

    return next_step, curr
        
def get_start():
    if pipe_map[start[0]][start[1] - 1] in ['-', 'L', 'F']:
        return [start[0], start[1] - 1]
    if pipe_map[start[0]][start[1] + 1] in ['-', 'L', 'F']:
        return [start[0], start[1] + 1]
    return [start[0] + 1, start[1]]

def play_game():
    back_at_start = False
    steps = 0
    curr = get_start()
    prior = start

    while not back_at_start:
        curr, prior = get_next(curr, prior)
        steps += 1
        if curr == start:
            back_at_start = True

    return steps

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    start, pipe_map = get_input(lines)

    steps = play_game()
    print((steps + 1) / 2)