def eight_queens(_set, placed, row):
    if row > 7:
        _set.add(tuple(placed))
        return
    for col in range(8):
        if not colides(placed, row, col):
            eight_queens(_set, placed + [col], row + 1)

def colides(placed, row, col):
    for _row, _col in enumerate(placed):
        if _col == col or abs((_row - row) / (_col - col)) == 1:
            return True
    return False
    
def main():
    _set = set()
    eight_queens(_set, [], 0)
    print(len(_set))

if __name__ == '__main__':
    main()
