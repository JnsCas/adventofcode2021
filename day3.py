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


def get_filter_by_rating_type(rating_type):
    if rating_type == 'oxygen':
        return '1'
    return '0'


def get_rating_by_type(codes, rating_type):
    code_length = len(codes[0])
    bit_start_position = 0
    while bit_start_position < code_length:
        bit_position = bit_start_position
        codes_filtered = codes
        while bit_position < code_length and len(codes_filtered) > 0:
            sum_result = count_ones_and_zeros(codes_filtered, bit_position)
            bit_to_filter = get_bit_to_filter(sum_result, rating_type)
            codes_filtered = list(filter(lambda code_record: code_record[bit_position] == bit_to_filter, codes_filtered))
            if len(codes_filtered) == 1:
                return codes_filtered[0]
            bit_position += 1
        bit_start_position += 1
    return None


def get_bit_to_filter(sum_result, rating_type):
    if rating_type == 'oxygen':
        if sum_result['ones'] >= sum_result['zeros']:
            return '1'
        return '0'
    else:
        if sum_result['ones'] >= sum_result['zeros']:
            return '0'
        return '1'


def count_ones_and_zeros(codes, bit_position):
    sum_ones_and_zeros = {'zeros': 0, 'ones': 0}
    for code in codes:
        bit = code[bit_position]
        if bit == '0':
            sum_ones_and_zeros['zeros'] += 1
        else:
            sum_ones_and_zeros['ones'] += 1
    return sum_ones_and_zeros


def part_2():
    with open('input_day3.txt') as f:

        codes = []
        for line in f:
            code = str(line).rstrip()
            codes.append(code)

        oxygen_generator_rating = get_rating_by_type(codes, 'oxygen')
        co2_scrubber_rating = get_rating_by_type(codes, 'co2')

        return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
