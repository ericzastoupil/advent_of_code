def split_line(line):
    split = line[line.find(':') + 1:].split('|')
    winning = split[0].strip().split(" ")
    mine = split[1].strip().split(" ")

    for element in winning:
        if element == '':
            winning.remove('')

    for element in mine:
        if element == '':
            mine.remove('')

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