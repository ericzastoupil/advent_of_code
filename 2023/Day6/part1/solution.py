def get_lists(lines):
    time = ''
    distance = ''

    for line in lines:
        split_type = line.split(":")
        if "Time" in split_type[0]:
            times = split_type[1].strip()
            times = times.split()
    
        if "Distance" in split_type[0]:
            distances = split_type[1].strip()
            distances = distances.split()

    return times, distances

def get_winnable(time, distance):
    winnable = 0
    for charge_time in range(time):
        traveled = charge_time * (time - charge_time)
        if traveled > distance:
            winnable += 1
    return winnable

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    times, distances = get_lists(lines)

    winnable = 1
    for i in range(len(times)):
        winnable *= get_winnable(int(times[i]), int(distances[i]))

    print(winnable)