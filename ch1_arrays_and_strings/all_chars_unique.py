def are_all_chars_unique(strr):
    """without using additional data structures"""
    for index in range(len(strr) - 1):
        c = strr[index]
        if _contains(strr[index + 1:], c):
            return False
    return True

def _contains(s, c):
    for i in s:
        if c == i:
            return True
    return False

def quick_check(s):
    return len(set(s)) == len(s)

def main():
    strings = 'abcdef', 'abcda', '', 'a'
    for s in strings:
        print are_all_chars_unique(s) == quick_check(s)

if __name__ == '__main__':
    main()
