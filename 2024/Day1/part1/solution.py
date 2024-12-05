
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

    sum = 0
    for i in range(len(left)):
        sum += abs(left[i]-right[i])

    print ("Solution: " + str(sum))