def split_line(line):
    split = line[line.find(':') + 1:].split('|')
    winning = [i for i in split[0].strip().split(" ") if i != '']
    mine = [i for i in split[1].strip().split(" ") if i != '']

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