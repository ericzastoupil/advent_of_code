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

    card_counts = [1] * len(lines)
    card_counts.insert(0, 0)
    
    for num, card in enumerate(lines):
        winning, mine = split_line(card)
        count_winners = 0
        for winner in winning:
            if winner in mine:
                count_winners += 1
        for copy in range(1, count_winners + 1):
            card_counts[num + 1 + copy] += card_counts[num + 1]
    
    print(sum(card_counts))