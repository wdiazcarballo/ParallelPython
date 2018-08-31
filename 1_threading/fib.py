class Fib:
    a, b, n  = 0, 1, 10
    def __init__(self, n):
        self.n = n

    def fibonacci(self):
        print(self.a, self.b, end=' ')
        for i in range(self.n):
            self.a, self.b = self.b, self.a+self.b
            print(self.b, end=' ')
        return self.b

class Duck:
    times = 1
    def __init__(self, n):
        self.times = n
    def quack(self):
        for i in range(self.times):
            print('quack quack')


def main():
    fib = Fib(10)
    b = fib.fibonacci()
    print(f'\nb = {b}')

    donald = Duck(5)
    donald.quack()

if __name__ == '__main__':main()
    