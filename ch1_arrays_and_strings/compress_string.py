def compress_string(s):
    can_compress = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
            can_compress = True
            break
    if not can_compress:
        return s

    count = 1
    last = s[0]
    compressed = ''
    for c in s[1:]:
        if c == last:
            count += 1
        else:
            compressed += last + str(count)
            last = c
            count = 1
    compressed += last + str(count)
    return compressed

def main():
    stings = []
    stings.append("")
    stings.append("a")
    stings.append("ab")
    stings.append("aab")
    stings.append("aabb")
    stings.append("aaabb")
    stings.append("aabcccccaaa")
    for s in stings:
        print '\n'
        print 'Before: ', s
        print 'After:  ', compress_string(s)

if __name__ == '__main__':
    main()
