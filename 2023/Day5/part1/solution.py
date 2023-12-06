def get_seeds(line):
    seeds = line[line.find(':') + 1:].strip().split()
    seed_list = []
    for seed in seeds:
        seed_list.append(int(seed))

    return seed_list

def get_map(title):
    
    temp_list = []
    read = False
    for line in lines:
        if title in line:
            read = True
        elif read:
            if line == '\n':
                read = False
            else:
                temp_list.append(line.strip().split())

    return temp_list

def get_value(num, maps):
    for map in maps:
        dst_start = int(map[0])
        src_start = int(map[1])
        r = int(map[2])
        if num >= src_start and num < src_start + r:
            i = num - src_start
            return dst_start + i
    return num

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    first_line = file.readline()
    lines = file.readlines()

    seeds_list = get_seeds(first_line)
    soil_list = get_map('seed-to-soil')
    fertilizer_list = get_map('soil-to-fertilizer')
    water_list = get_map('fertilizer-to-water')
    light_list = get_map('water-to-light')
    temperature_list = get_map('light-to-temperature')
    humidity_list = get_map('temperature-to-humidity')
    location_list = get_map('humidity-to-location')

    lowest_location = -1
    for seed in seeds_list:
        soil = get_value(seed, soil_list)
        fertilizer = get_value(soil, fertilizer_list)
        water = get_value(fertilizer, water_list)
        light = get_value(water, light_list)
        temperature = get_value(light, temperature_list)
        humidity = get_value(temperature, humidity_list)
        location = get_value(humidity, location_list)

        if lowest_location == -1 or location < lowest_location:
            lowest_location = location

    print(lowest_location)