def find_max(number):
    maximum=number[0]
    for x in number:
        if x>maximum:
            maximum=x
    return maximum