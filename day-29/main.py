import string
import random




class PassGen:
    def generator(self,length):
        letter = string.ascii_letters
        number = string.digits
        punct = string.punctuation

        pas = letter + number + punct

        ret = ""
        for i in range(length):
            ret = ret + random.choice(pas)
            
            
        return ret


pg = PassGen()
a = int(input("enter a number:"))
result = pg.generator(a)
print (result)