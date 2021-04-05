def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
                pass
    return False

print(check_even_list([1,3,5,7,9]))
