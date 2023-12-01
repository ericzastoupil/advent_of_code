def find_first_word(words, line):
    idx = -1
    final_word = ''
    for word in words:
        if word in line:
            if idx == -1 or line.find(word) < idx:
                idx = line.find(word)
                final_word = word

    return final_word, idx

def find_last_word(words, line):
    idx = -1
    final_word = ''

    for word in words:
        if word in line:
            if idx == -1 or line.rindex(word) > idx:
                idx = line.rindex(word)
                final_word = word

    return final_word, idx

def find_first_digit(line):
    for i, char in enumerate(line):
        if char.isdigit():
            return char, i
    return '', -1

def find_last_digit(line):
    for char in range(len(line) - 1, -1, -1):
        if line[char].isdigit():
            return line[char], char
    return '', -1

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    words_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    coordinates = []
    for line in lines:
        first_digit, digit_idx = find_first_digit(line)
        first_word, word_idx = find_first_word(words, line)

        if digit_idx == -1:
            first = words_dict[first_word]
        elif word_idx == -1:
            first = first_digit
        elif word_idx < digit_idx:
            first = words_dict[first_word]
        elif digit_idx < word_idx:
            first = first_digit

        last_digit, digit_idx = find_last_digit(line)
        last_word, word_idx = find_last_word(words, line)

        if digit_idx == -1:
            second = words_dict[last_word]
        elif word_idx == -1:
            second = last_digit
        elif word_idx > digit_idx:
            second = words_dict[last_word]
        elif digit_idx > word_idx:
            second = last_digit

        coordinates.append(int(first + second))

    print ("Solution: " + str(sum(coordinates)))
