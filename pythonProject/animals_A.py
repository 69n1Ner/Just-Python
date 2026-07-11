
class Pet:
    def __init__(self, petName, petAge):
        self.__name = petName
        self.__age = petAge
        if not hasattr(self, 'say'):
            raise NotImplementedError("Нельзя создать такой объект!")

    def gettingOlder(self):
        self.__age += 1

    name = property(lambda x: x.__name)
    age = property(lambda x: x.__age)


class Cat(Pet):
    def __init__(self,petName,petAge):
        Pet.__init__(self, petName, petAge)



    def say(self):
        print(f'{self.name}: Мяу!')


class Dog(Pet):
    def __init__(self, petName, petAge):
        Pet.__init__(self,petName, petAge)


    def say(self):
        print(f'{self.name}: Гав!')



