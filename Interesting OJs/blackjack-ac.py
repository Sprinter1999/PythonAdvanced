class card:
    prior_color = {
        'Spade': 1,
        'Heart': 2,
        'Diamond': 3,
        'Club': 4
    }
    prior_number = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13
    }
    
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.prior_color = card.prior_color[color]
        self.prior_number = card.prior_number[number]
        
    def get_point(self):
        if self.number >= '2' and self.number <= '9':
            return int(self.number)
        elif self.number != 'A':
            return 10
        else:
            return 1
        
    def printwithoutspace(self):
        print('{}{}'.format(self.color, self.number), end='')
        
class hand:
    def __init__(self):
        self.cardlist = []
        self.point = 0
        self.A11 = False
    
    def get_point(self):
        return self.point
    
    def set_point(self, point):
        self.point = point
    
    def add_card(self, card):
        self.cardlist.append(card)
        card_point = card.get_point()
        total_point = self.get_point()
        if card_point != 1:
            if total_point + card_point <= 21:
                self.set_point(total_point + card_point)
            elif self.A11:
                self.set_point(total_point + card_point - 10)
                self.A11 = False
            else:
                self.set_point(total_point + card_point)
            return '{} {}'.format(card.color, card_point)
        else:
            if total_point + 11 <= 21:
                self.set_point(total_point + 11)
                self.A11 = True
            else:
                self.set_point(total_point + 1)
            return '{} 1 11'.format(card.color)
    
    def blackjack(self):
        point1 = self.cardlist[0].get_point()
        point2 = self.cardlist[1].get_point()
        if point1 > point2:
            point1, point2 = point2, point1
        if point1 == 1 and point2 == 10:
            return True
        return False
    
    def printlist(self):
        self.cardlist = sorted(self.cardlist, key=lambda x: (x.prior_number, x.prior_color))
        for i in range(len(self.cardlist)):
            self.cardlist[i].printwithoutspace()
            if i == len(self.cardlist) - 1:
                print('\n', end='')
            else:
                print(' ', end='')
        
cnt = 0
cur_hand = hand()
while True:
    try:
        now_card = card(*list(input().split()))
        cnt = cnt + 1
        if cnt <= 2:
            cur_hand.add_card(now_card)
            total_point=cur_hand.get_point()
            #还得考虑最后只有两种输入的情况
            if total_point >= 17:
                print('Stand')
                if total_point > 21:
                    cur_hand.printlist()
                    print('Bust')
                elif cur_hand.blackjack():
                    cur_hand.printlist()
                    print('Blackjack')
                else:
                    cur_hand.printlist()
                    print(total_point)
            continue
        total_point = cur_hand.get_point()
        if total_point < 17:
            print('Hit')
            print(cur_hand.add_card(now_card))
            total_point = cur_hand.get_point()
        if total_point >= 17:
            print('Stand')
            if total_point > 21:
                cur_hand.printlist()
                print('Bust')
            elif cur_hand.blackjack():
                cur_hand.printlist()
                print('Blackjack')
            else:
                cur_hand.printlist()
                print(total_point)
            break
    except:
        break