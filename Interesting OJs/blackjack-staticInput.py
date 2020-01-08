class Card:
    def __init__(self, card_type:str, card_value:str):
        self.card_type = card_type
        self.card_value = card_value
        self.card_amount=0
        self.priority=1
        if(card_value=="J" or card_value=="Q" or card_value=="K"):
            self.card_amount=10
            self.priority=10
        elif(card_value=="A"):#如果是A则先当成0，然后动态计算
            pass
        else:
            self.card_amount=eval(card_value)
            self.priority=eval(card_value)
class Hand:
    def __init__(self):
        self.cards=[]

class Player():
    def __init__(self):
        self.total=0
        self.owned=[] #stores cards
        self.sumt=0
    def calc(self):
        tempStorage=[]
        self.sumt=0
        # print("init",self.sumt)
        # print("内部有几个？",len(self.owned))
        for i in range(len(self.owned)):
            if(self.owned[i].card_value!="A"):
                #说明不是A
                self.sumt+=self.owned[i].card_amount
                # print("not A",self.owned[i].card_amount,self.sumt)
            else:
                tempStorage.append(self.owned[i])
                #说明是A,放到最后处理                             
        for i in range(len(tempStorage)):
            if(self.sumt+11<=21):
                self.sumt+=11
                # self.owned[i].card_amount=11
            else:
                self.sumt+=1
                # self.owned[i].card_amount=1
            # print("A",self.owned[i].card_amount,self.sumt)
        return self.sumt
       
    def check(self):
        temp=self.sumt
        if(temp==21):
            return 0 #which means Blackjack
        elif(temp>21):
            return 1 #which means Burst
        elif(temp<17):
            return -2 #which means less than 17 and needs more card
        elif(17<=temp<=20):
            return -1 #which means between [17,21)
    def output(self):
        anotherLis=sorted(self.owned,key=lambda card:(-card.priority,card.card_value),reverse=True)
        for each in anotherLis:
            print(each.card_type+each.card_value,end=" ")#need testing
        print()
        if(self.sumt==21):
            print("Blackjack")
        elif(self.sumt>21):
            print("Bust")
        else:        
            print(self.sumt)

Hand=Hand()
Player=Player()

aTup=tuple(input().split())
while(True):
    if not aTup:
        break
    else:
        Hand.cards.append(aTup)
        aTup=tuple(input().split())

for i in range(len(Hand.cards)):
    tmp=Hand.cards[i]
    if(i==0 or i==1):
        tmpCard=Card(tmp[0],tmp[1])
        Player.owned.append(tmpCard)
    else:
        Player.calc()
        checker=Player.check()
        if(checker!=-2):
            print("Stand")
            Player.output() #保证output前先calc，更新sumt信息
            break
        else:
            print("Hit")
            tmpCard=Card(tmp[0],tmp[1])
            print(tmp[0],tmp[1])
            Player.owned.append(tmpCard)
            # 更新后再算一次
            Player.calc()
            checker=Player.check()
            # print(len(Player.owned))
            # print(checker)
            # print(Player.sumt)
            if(checker!=-2):
                print("Stand")
                Player.output() #保证output前先calc，更新sumt信息
                break