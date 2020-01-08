# 如果手中牌的点数之和小于17点则继续要下一张牌，直到大于等于17点为止
# 如果手里的牌有A，且A的点数当成11点没有超过21点，则此时A要按11点计算，如果超过21点，则A要按1点计算
# 1、设计一个card类，用于保存一张牌；
# 2、设计一个hand类，用于保存一手牌；
# 3、设计一个player类，该类可以基于指定策略完成一次游戏过程。
# 读入前两张牌不输出，从第三张牌开始 如果需要
# 则每次要牌，要先输出Hit，然后读入下一张牌
# 并依次输出该牌的花色及点数（A输出1 11，即它有两个点数）
# 当不再要牌时要先输出Stand，然后在一行内输出这一手牌，牌与牌之间用一个空格分隔。牌输出的顺序为先看牌面，牌面小的在前（牌面由小到大的顺序为A,2,3....J,Q,K）


class Card:
    # real_point代表比赛用的点数，virtual point表示点数的名称，point表示数学意义上的点数
    def __init__(self, pattern: str, virtual_point: str):
        self.virtual_point = virtual_point
        self.pattern = pattern
        self.init()

    def init(self):
        if (self.virtual_point == 'A'):
            self.real_point = 1
            self.point = 1
        elif self.virtual_point == 'J':
            self.real_point = 10
            self.point = 11
        elif self.virtual_point == 'Q':
            self.real_point = 10
            self.point = 12
        elif self.virtual_point == 'K':
            self.real_point = 10
            self.point = 13
        else:
            self.real_point = int(self.virtual_point)
            self.point = int(self.virtual_point)

    def __eq__(self, other):
        return self.point == other.point and self.pattern == other.pattern

    def __gt__(self, other):
        if (self.point < other.point):
            return False
        elif (self.point > other.point):
            return True
        else:
            if (self.pattern == 'Spade'):
                return False
            elif (self.pattern == 'Heart'):
                if other.pattern == 'Spade':
                    return True
                else:
                    return False
            elif (self.pattern == 'Diamond'):
                if (other.pattern == 'Club'):
                    return False
                else:
                    return True
            else:  # self.pattern ==Club
                return True

    def printPatternVirtualPoint(self):
        print(self.pattern + self.virtual_point, end="")

    def printPatternRealPoint(self):
        if (self.virtual_point == 'A'):
            print(self.pattern + ' 1 11')
        else:
            print(self.pattern + ' ' + str(self.real_point))


class Hand:
    def __init__(self):
        self.hand = []

    def append(self, card: Card):
        self.hand.append(card)
        self.hand.sort()

    def getTotalPoint(self):
        A_cnt = 0
        total_point = 0
        for i in self.hand:
            total_point += i.real_point
            if i.virtual_point == 'A':
                A_cnt += 1
        total_point += A_cnt * 10
        while(total_point > 21 and A_cnt > 0):
            total_point -= 10
            A_cnt -= 1
        return total_point

    def getAll(self):
        return self.hand

    def printAll(self):
        for i in self.hand:
            i.printPatternVirtualPoint()
            print(" ", end='')
        print('')


class Player:
    def __init__(self):
        pass

    def play(self):
        cnt = 0
        h = Hand()
        while (1):
            cnt += 1
            if cnt > 2:
                print("Hit")
            card = Card(*(input().split(' ')))
            h.append(card)
            if cnt > 2:
                card.printPatternRealPoint()
            if h.getTotalPoint() >= 17:
                print("Stand")
                break
        h.printAll()
        if (h.getTotalPoint() > 21):
            print("Bust")
        elif h.getTotalPoint() == 21 and len(h.hand) == 2:
            print("Blackjack")
        else:
            print(h.getTotalPoint())
            



if __name__ == "__main__":
    p = Player()
    p.play()