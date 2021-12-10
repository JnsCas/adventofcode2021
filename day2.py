def part_1():
    with open('input_day2.txt') as f:
        horizontal_position = 0
        depth_position = 0
        for line in f:
            [command, value_str] = line.split()
            value = int(value_str)
            if command == 'forward':
                horizontal_position += value
            elif command == 'up':
                depth_position -= value
            elif command == 'down':
                depth_position += value
    return horizontal_position * depth_position


def part_2():
    with open('input_day2.txt') as f:
        horizontal_position = 0
        depth_position = 0
        aim = 0
        for line in f:
            [command, value_str] = line.split()
            value = int(value_str)
            if command == 'forward':
                horizontal_position += value
                depth_position += aim * value
            elif command == 'up':
                aim -= value
            elif command == 'down':
                aim += value
    return horizontal_position * depth_position


if __name__ == '__main__':
    print(part_1())
    print(part_2())
