def get_t_d(lines):
    time = ''
    distance = ''

    for line in lines:
        split_type = line.split(":")
        if "Time" in split_type[0]:
            times = split_type[1].strip()
            times = times.split()
            for t in range(len(times)):
                time = time + times[t]
            time = int(time)
                
        if "Distance" in split_type[0]:
            distances = split_type[1].strip()
            distances = distances.split()
            for d in range(len(distances)):
                distance = distance + distances[d]
            distance = int(distance)

    return time, distance

def get_winnable(time, distance):
    winnable = 0
    for charge_time in range (time):
        traveled = charge_time * (time - charge_time)
        if traveled > distance:
            winnable += 1
    return winnable

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    time, distance = get_t_d(lines)

    winnable = get_winnable(time, distance)

    print(winnable)