def color_is_valid(color):
    color_cubes = color.split(" ")
    if 'red' in color_cubes and int(color_cubes[1]) > 12:
        return False
    elif 'green' in color_cubes and int(color_cubes[1]) > 13:
        return False
    elif 'blue' in color_cubes and int(color_cubes[1]) > 14:
        return False
    return True

def round_is_valid(round):
    colors = round.split(',')
    for color in colors:
        if not color_is_valid(color):
            return False
    return True

def game_is_valid(game):
    rounds = game.split(';')
    for round in rounds:
        if not round_is_valid(round):
            return False
    return True

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    valid_games = []
    for line in lines:
        split_line = line.split(':')
        game_number = split_line[0].split(' ')[1]
        if game_is_valid(split_line[1]):
            valid_games.append(int(game_number))
    
    print(sum(valid_games))