def game_power(game):
    max_red = 0
    max_green = 0
    max_blue = 0

    rounds = game.split(';')
    for round in rounds:
        colors = round.split(',')
        for color in colors:
            color.strip()
            cubes = color.split()

            if 'red' in cubes and int(cubes[0]) > max_red:
                max_red = int(cubes[0])
            elif 'green' in cubes and int(cubes[0]) > max_green:
                max_green = int(cubes[0])
            elif 'blue' in cubes and int(cubes[0]) > max_blue:
                max_blue = int(cubes[0])

    return max_red * max_green * max_blue

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    game_powers = []
    for line in lines:
        split_line = line.split(':')
        game_powers.append(game_power(split_line[1]))
    
    print(sum(game_powers))