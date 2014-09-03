def is_rotation(s1, s2):
    s = s1 + s1
    if len(s1) == len(s2):
        return is_substring(s, s2)
    return False

def is_substring(s1, s2):
    return s2 in s1

def main():
    origin = 'waterbottle'
    strings = []
    strings.append('')
    strings.append('aterbottle')
    strings.append('aterbottlew')
    strings.append('ottlewaterb')
    strings.append('waterbottle')
    strings.append('this_must_not_be')
    for s in strings:
        print "'{}' is a rotation of '{}': ".format(s, origin), is_rotation(origin, s)

if __name__ == '__main__':
    main()
