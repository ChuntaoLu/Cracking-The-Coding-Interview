def is_permutation(s1, s2):
    """O(nlogn)"""
    return sorted(s1) == sorted(s2)

def is_permutation_faster(s1, s2):
    """O(n), assuming chars in string are ascii"""
    count = [0 for _ in range(256)]
    for i in s1:
        count[ord(i)] += 1

    for i in s2:
        count[ord(i)] -= 1
        if count[ord(i)] < 0:
            return False
    return True


def main():
    print is_permutation('this', 'isht') == True
    print is_permutation('this ', 'i sht') == True
    print is_permutation('th', 'i sht') == False
    print is_permutation('', '') == True
    print is_permutation_faster('this', 'isht') == True
    print is_permutation_faster('this ', 'i sht') == True
    print is_permutation_faster('th', 'i sht') == False
    print is_permutation_faster('', '') == True

if __name__ == '__main__':
    main()
