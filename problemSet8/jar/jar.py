class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int) or capacity<0:
            raise ValueError()
        self.cap = capacity
        self.cookies=0

    def __str__(self):
        return '🍪'*self.cookies

    def deposit(self, n):
        if self.cookies+n > self.cap:
            raise ValueError()
        self.cookies+=n


    def withdraw(self, n):
        if self.cookies-n < 0 :
            raise ValueError()
        self.cookies-=n

    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.cookies
