from basic.deque import Deque


def palchecker(strings):
    adeque = Deque()

    for str in strings:
        adeque.addRear(str)

    stillequal = True

    while adeque.size() > 1 and stillequal:
        first = adeque.removeFront()
        last = adeque.removeRear()

        if first == last:
            stillequal = True
        else:
            stillequal = False

    return stillequal


if __name__ == "__main__":
    print(palchecker("abcba"))
    print(palchecker("asdfrde"))
