from string_class import string


if __name__ == '__main__':
    some_string = string.String(['H', 'e', 'l', 'l', 'o'])
    another_string = string.String([' ', 'W', 'o', 'r', 'l', 'd', '!'])

    print(some_string)

    some_string.append('!')
    print(some_string)

    some_string.insert(5, ' ')
    print(some_string)

    some_string.remove('!')
    print(some_string)

    some_string.replace('H', 'W')
    print(some_string)

    some_string.reverse()
    print(some_string)

    some_string.upper()
    print(some_string)

    some_string.lower()
    print(some_string)

    sum_string = some_string + another_string
    print(f'Strings sum: {sum_string}')

    mul_string = some_string * 4
    print(f'Strings mul: {mul_string}')

    file_string = string.String.read_file('random_text.txt')
    print(f'String from file: {file_string}')

    index = some_string.index('l')
    print(f'L letter index: {index}')
