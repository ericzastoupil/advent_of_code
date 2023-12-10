def get_input(lines):
    values= []
    for line in lines:
        values.append([int(x) for x in line.split()])

    return values

def do_it(values):
    diffs = []
    for i in range(1,len(values),1):
        diffs.append(values[i] - values[i-1])

    if set(diffs) == {0}:
        return values[-1] + 0
    else:  
        return values[-1] + do_it(diffs)   

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    value_sets = get_input(lines)

    extraploted_values = []
    for values in value_sets:
        values.reverse()
        extraploted_values.append(do_it(values))
    
    print(sum(extraploted_values))