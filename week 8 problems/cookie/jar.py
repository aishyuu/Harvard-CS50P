"""
Create a class called Jar with the following methods
    __init__ with capacity (max number of cookies that can fit in the cookie jar)
        Non negative integer
    __str__ should return a string with n🍪 (number of cookies in the jar)
        If there are 3 cookies, then it should return 🍪🍪🍪
    deposit should add n cookies to the cookie jar
        If adding n cookies exceeds the capacity, deposit should raise a value error
    withdraw removes n cookies from the jar
        If there aren't that many cookies in a jar, withdraw should raise a value error
    capacity should return the cookie jar's capacity
    size should return the number of cookies currently in the cookie jar
"""

class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        if self.cookies == 0:
            return("")
        return("🍪" * self.cookies)

    def deposit(self, n):
        if (n+self.cookies) > self.capacity:
            raise ValueError("Total cookies passes cookie capacity for this jar")
        self.cookies += n

    def withdraw(self, n):
        if(self.cookies - n) < 0:
            raise ValueError("Cookies withdrawn is more than the number of cookies in jar")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self.cookies

def main():
    test = Jar()
    print(test)

if __name__ == "__main__":
    main()