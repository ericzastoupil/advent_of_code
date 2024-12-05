def evaluate(r):
    #Determine if the list is increasing or decreasing
    #If first two values are the same, move on to the next line
    if r[0] == r[1]:
        return False
    #If first value is higher than second value, it is decreasing.
    elif r[0] > r[1]:
        dec = True
    else:
        dec = False
        
    #Evaluate the report
    for i in range(len(r)):
        if i == len(r) - 1:
            return True
        elif r[i] > r[i + 1] and dec:
            if r[i] - r[i + 1] > 3:
                return False
        elif r[i] < r[i + 1] and not dec:
            if r[i + 1] - r[i] > 3:
                return False
        else:
            return False

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()

    safe = 0
    for line in lines:
        report = [int(x) for x in line.split(" ")]
        if evaluate(report):
            safe += 1      

    print ("Solution: " + str(safe))