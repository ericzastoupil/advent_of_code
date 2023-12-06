
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

def get_reverse(num, maps):
    for map in maps:
        dst_start = int(map[1])
        src_start = int(map[0])
        r = int(map[2])
        if num >= src_start and num < src_start + r:
            i = num - src_start
            return dst_start + i
    return num

def location_to_seed(location):
    humidity = get_reverse(location, location_list)
    temperature = get_reverse(humidity, humidity_list)
    light = get_reverse(temperature, temperature_list)
    water = get_reverse(light, light_list)
    fertilizer = get_reverse(water, water_list)
    soil = get_reverse(fertilizer, fertilizer_list)
    seed = get_reverse(soil, soil_list)

    return seed

def check_valid(start_seed):
    for i in range(0, len(seeds_list), 2):
        if start_seed >= seeds_list[i] and start_seed < seeds_list[i] + seeds_list[i + 1]:
            return True
    return False

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

    end_loc = 1
    valid_start = False
    while not valid_start:
        end_loc += 1
        start_seed = location_to_seed(end_loc)
        valid_start = check_valid(start_seed)
    print(end_loc)