def split_line(line):
    split = line[line.find(':') + 1:].split('|')
    winning = [i for i in split[0].strip().split(" ") if i != '']
    mine = [i for i in split[1].strip().split(" ") if i != '']

    return winning, mine

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    final = 0
    
    for line in lines:
        winning, mine = split_line(line)
        game = 0

        for winner in winning:
            if winner in mine:
                if game == 0:
                    game += 1
                else:
                    game *= 2
        final += game
    
    print(final)