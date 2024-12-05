
if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()

    left = []
    right = []
    for line in lines:
        left.append(int(line.split(' ')[0]))
        right.append(int(line.split()[1]))

    left.sort()
    right.sort()

    similarity = 0
    for l in left:
        for r in right:
            if l == r:
                similarity += l

    print ("Solution: " + str(similarity))