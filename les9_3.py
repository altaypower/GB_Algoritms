"""
функция из урока
"""

def my_index(value):
    letter = 26
    index = 0
    size = 10000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter**i

    return  index%size

a='apricot'
b='banana'
print(my_index(a))
print(my_index(b))