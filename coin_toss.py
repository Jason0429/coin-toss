import random


class Coin:
    def __init__(self):
        self.__tosses = []

    def toss(self):
        rand_int = random.randint(0, 10)
        side = "Heads" if rand_int > 5 else "Tails"
        return side

    def append_toss(self, side):
        self.__tosses.append(side)

    def append_tosses(self, arr):
        self.__tosses.extend(arr)

    def get_tosses(self):
        return self.__tosses

    def get_heads_count(self, arr):
        count = 0
        for side in arr:
            if side == 'Heads':
                count += 1
        return count

    def get_tails_count(self, arr):
        count = 0
        for side in arr:
            if side == 'Tails':
                count += 1
        return count

    def clear_tosses(self):
        self.__tosses.clear()

    def repeat_tosses(self, times):
        arr = []
        for i in range(times):
            arr.append(self.toss())
        return arr

    def get_difference(self, arr):
        return float(abs(self.get_heads_count(arr) - self.get_tails_count(arr))) / len(arr)


if __name__ == '__main__':
    c = Coin()
    c.append_tosses(c.repeat_tosses(100))
    heads = c.get_heads_count(c.get_tosses())
    tails = c.get_tails_count(c.get_tosses())

    print("Number of heads: {}".format(heads))
    print("Number of tails: {}".format(tails))
    print("Percent difference: {}".format(c.get_difference(c.get_tosses())))
