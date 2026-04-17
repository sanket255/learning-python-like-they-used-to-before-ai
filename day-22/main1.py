class Counter:
    def __init__(self,current):
        self.current=current
    def increment(self,inc):
        self.current+=inc
    def decrement(self,dec):
        self.current-=dec
    def info(self):
        print(f"{self.current}")

count = Counter(0)

count.increment(1)
count.increment(1)
count.decrement(1)
count.info()