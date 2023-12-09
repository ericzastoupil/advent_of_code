def get_players(lines):
    hands_dict = {}
    for i in range(len(lines)):
        split = lines[i].strip().split()
        temp_list = []
        for j in range(len(split[0])):
            temp_list.append(split[0][j])
        hands_dict[i] = {}
        hands_dict[i]['hand'] = temp_list
        hands_dict[i]['bid'] = int(split[1])
    return hands_dict

def get_strength(hand):
    temp_dict = {i:hand.count(i) for i in hand}
    threes = 0
    twos = 0
    for key in temp_dict:
        if temp_dict[key] == 5 or temp_dict[key] == 4:
            return temp_dict[key] + 1
        if temp_dict[key] == 3:
            threes += 1
        if temp_dict[key] == 2:
            twos += 1
    if threes == 1:
        if twos == 1:
            return 4
        else:
            return 3
    if twos == 2:
        return 2
    if twos == 1:
        return 1
    return 0
        
def assign_hand_strength(players):
    for player in players:
        hand = players[player]['hand']
        players[player]['strength'] = get_strength(hand)

def translate_card_strength(card):
    if card.isdigit():
        return int(card)
    else:
        if card == 'A':
            return 14
        elif card == 'K':
            return 13
        elif card == 'Q':
            return 12
        elif card == 'J':
            return 11
        elif card == 'T':
            return 10
        
def sort_within_strength_groups(hands):
    l = sorted(hands, key = lambda x: (translate_card_strength(x[0]), 
                                       translate_card_strength(x[1]), 
                                       translate_card_strength(x[2]), 
                                       translate_card_strength(x[3]), 
                                       translate_card_strength(x[4])))
    return l

def group_by_hand_strength(players):
    hands_by_strength = {'zeroes' : [],
                         'ones' : [],
                         'twos' : [], 
                         'threes' : [],
                         'fours' :[],
                         'fives' : [],
                         'sixes' : [],}

    for key in players:
        if players[key]['strength'] == 0:
            hands_by_strength['zeroes'].append(players[key]['hand'])
        if players[key]['strength'] == 1:
            hands_by_strength['ones'].append(players[key]['hand'])
        if players[key]['strength'] == 2:
            hands_by_strength['twos'].append(players[key]['hand'])
        if players[key]['strength'] == 3:
            hands_by_strength['threes'].append(players[key]['hand'])
        if players[key]['strength'] == 4:
            hands_by_strength['fours'].append(players[key]['hand'])
        if players[key]['strength'] == 5:
            hands_by_strength['fives'].append(players[key]['hand'])
        if players[key]['strength'] == 6:
            hands_by_strength['sixes'].append(players[key]['hand'])

    return hands_by_strength

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    players = get_players(lines)
    assign_hand_strength(players)
    hands_by_strength = group_by_hand_strength(players)

    hands_low_to_high = []
    for key in hands_by_strength:
        hands_low_to_high.extend(sort_within_strength_groups(hands_by_strength[key]))

    final = 0
    count = 1
    for hand in hands_low_to_high:
        for key in players:
            if players[key]['hand'] == hand:
                final += players[key]['bid'] * count
                count += 1

    non_point = 0
    for key in players:
        if players[key]['strength'] == 0:
            non_point += 1

    print(final)
