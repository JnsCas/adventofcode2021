def revert_bit(bit):
    if bit == '1':
        return '0'
    return '1'


def revert_binary(binary):
    binary_length = len(binary)
    result = ''
    for index in range(binary_length):
        result += revert_bit(binary[index])
    return result


def get_gamma_rate_bit(total_sum):
    if total_sum > 0:
        return '1'
    return '0'


def get_number_to_sum(bit):
    if bit == '1':
        return 1
    return -1


def part_1():
    with open('input_day3.txt') as f:
        code_length = len(f.readline().rstrip())

        # init sum_array
        sum_array = [0] * code_length

        for line in f:
            code = str(line).rstrip()
            for index in range(code_length):
                bit = code[index]
                sum_array[index] += get_number_to_sum(bit)

        gamma_rate = ''
        for index in range(code_length):
            gamma_rate += get_gamma_rate_bit(sum_array[index])
        gamma_rate_decimal = int(gamma_rate, 2)

        epsilon_rate = revert_binary(gamma_rate)
        epsilon_rate_decimal = int(epsilon_rate, 2)
        return gamma_rate_decimal * epsilon_rate_decimal  # power consumption


if __name__ == '__main__':
    print(part_1())
