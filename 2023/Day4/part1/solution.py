def split_line(line):
    split = line[line.find(':') + 1:].split('|')
    winning = [i for i in split[0].strip().split(" ") if i != '']
    mine = [i for i in split[1].strip().split(" ") if i != '']

    return winning, mine

def game_score(wining, mine):
    game = 0

    for winner in winning:
        if winner in mine:
            if game == 0:
                game += 1
            else:
                game *= 2
    
    return game

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    final = 0
    
    for line in lines:
        winning, mine = split_line(line)

        final += game_score(winning, mine)
    
    print(final)