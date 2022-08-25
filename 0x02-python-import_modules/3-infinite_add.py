#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for a in sys.argv:
        if a != sys.argv[0]:
            total += int(a)
    print(total)
