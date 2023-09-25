def solution(my_string):
    str = ['a', 'e', 'i', 'o', 'u']
    for i in str:
        my_string = my_string.replace(i, '')
    return my_string