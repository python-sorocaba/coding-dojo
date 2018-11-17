def sum_squares(list_numbers):
    sum_numbers = 0
    for num in list_numbers:
        sum_numbers += num ** 2
    return sum_numbers


def split_number(number):
    str_number = str(number)
    list_split = []
    for char in str_number:
        list_split.append(int(char))
    return list_split


def happy_number(number, saved_nums=None):
    if saved_nums is None:
        saved_nums = []

    if number == 1 or number == 7:
        return True

    split_num = split_number(number)
    num_sum = sum_squares(split_num)
    if num_sum in saved_nums:
        return False
    else:
        saved_nums.append(num_sum)
        return happy_number(num_sum, saved_nums)
