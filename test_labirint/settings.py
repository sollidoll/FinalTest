def gen_str(n):
    return 'x' * n

def gen_num_str(n):
    return '3' * n


valid_str = 'Агата'
space_str = ' '
only_nums = '1234'
str_255 = gen_str(255)
str_1000 = gen_str(1000)
chinese_str = '的一是不了人我在有他这为之大来以个中上们'
spec_symbol = r'|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

data_for_search = [valid_str, space_str, only_nums, str_255, str_1000, chinese_str, spec_symbol]
cases_for_search = ['valid_input', 'space_string', 'only_nums', 'string_255', 'string_1000', 'chinese_string', 'special_symbols']

str_50 = gen_str(50)
str_51 = gen_str(51)

data_for_ordering = [valid_str, space_str, only_nums, str_50, str_51, str_255, str_1000, chinese_str, spec_symbol]
cases_for_ordering = ['valid_input', 'space_string', 'only_nums', 'string_50', 'string_51', 'string_255', 'string_1000', 'chinese_string', 'special_symbols']

correct_number = '+375 29 123 23 23'
number_without_one_num = '+375 29 123 23 2'
number_with_one_extra_num = '+375 29 123 23 231'
number_with_minus = '-375 29 123 23 23'
number_255 = gen_num_str(255)
number_1000 = gen_num_str(1000)

invalid_numbers = [correct_number, number_without_one_num, number_with_one_extra_num, number_with_minus, number_255, number_1000, space_str]
invalid_nums_cases = ['correct number', 'number without one num', 'number with one extra num', 'number with minus', 'number with 255 nums', 'number with 1000 nums', 'space string']