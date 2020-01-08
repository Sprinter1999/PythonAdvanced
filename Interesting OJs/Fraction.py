from fractions import Fraction
class Pair():
    def __init__(self,a,b,c,d):
        self.first=Fraction(a,b)
        self.second=Fraction(c,d)
    def display(self):
        print(str(self.first.numerator)+"/"+str(self.first.denominator))
        print(str(self.second.numerator)+"/"+str(self.second.denominator))
    def plus(self):
        plus=self.first+self.second
        print(str(plus.numerator)+"/"+str(plus.denominator))
    def substract(self):
        subs=self.first-self.second
        print(str(subs.numerator)+"/"+str(subs.denominator))
    def multiply(self):
        multi=self.first*self.second
        print(str(multi.numerator)+"/"+str(multi.denominator))
    def divide(self):
        div=self.first/self.second
        print(str(div.numerator)+"/"+str(div.denominator))
    def inverse(self):
        ans=Fraction(self.first.denominator,self.first.numerator)
        print(str(ans.numerator)+"/"+str(ans.denominator))
    def value(self):
        print("{:.1f}".format(self.first.numerator/self.first.denominator))
a,b,c,d=map(int,input().split())
pair=Pair(a,b,c,d)
pair.display()
pair.plus()
pair.substract()
pair.multiply()
pair.divide()
pair.inverse()
pair.value()