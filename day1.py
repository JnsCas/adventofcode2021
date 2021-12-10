def part_1():
    previous_measurement = -1
    total_increments = -1
    with open('input_day1.txt') as f:
        for line in f:
            measurement = int(line)
            if measurement > previous_measurement:
                total_increments += 1
            previous_measurement = measurement
    return total_increments


def part_2():
    with open('input_day1.txt') as f:
        previous_sum_window = -1
        total_increments = -1
        measurements = []
        init_window_index = 0
        window_size = 3
        for line in f:
            measurement = int(line)
            measurements.append(measurement)
            if len(measurements) > 2:
                window = measurements[init_window_index: init_window_index + window_size]
                sum_window = sum(window)
                if sum_window > previous_sum_window:
                    total_increments += 1
                init_window_index += 1
                previous_sum_window = sum_window
    return total_increments


if __name__ == '__main__':
    print(part_1())
    print(part_2())
