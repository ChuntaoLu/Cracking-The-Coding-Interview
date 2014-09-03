import re


def replace_spaces_regex(s):
    """using regular expression"""
    return re.sub('\s', '20%', s.strip())

def replace_spaces_inplace(s):
    """
    without using regex.
    Assume 's' is a char array, replace spaces in place.
    construct string by char array, and iterating backwards.
    """
    length = len(s)
    space_count = sum(1 for i in s if i == ' ')
    new_end = length + 2 * space_count
    s[length: new_end] = [''] * 2 * space_count
    for index in range(length - 1, -1, -1):
        if s[index] == ' ':
            s[new_end - 3: new_end] = list('%20')
            new_end -= 3
        else:
            s[new_end - 1] = s[index]
            new_end -= 1



def main():
    s = "Mr John  Smith   "
    new_s = replace_spaces_regex(s)
    print 'using regex: ', new_s
    print 'in place: '
    char_array = list(s.strip())
    print 'Before: ', ''.join(char_array)
    replace_spaces_inplace(char_array)
    print 'After: ', ''.join(char_array)

if __name__ == '__main__':
    main()
