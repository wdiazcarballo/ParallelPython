class Duck():
    sound = 'Quaaack!'
    walking = 'Walks like a duck.'
 
    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

def main():
    ducks = []

    for i in range(5):
        ducks.append(Duck())
    
    ducks[0].quack()


if __name__ == '__main__': main()