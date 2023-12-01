

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()

    coordinates = []
    for line in lines:
        for char in line:
            if char.isdigit():
                first = char
                break
        for char in reversed(line):
            if char.isdigit():
                second = char
                break

        coordinates.append(int(first + second))

    print ("Solution: " + str(sum(coordinates)))
