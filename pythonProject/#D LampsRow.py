class LampRow:
    def __init__(self,n1):
        self.n = n1
        self.__state = int('1' + '0' * self.n)

    def show(self):
        temp = str(self.__state)[1:]
        temp = temp.replace('0','-')
        temp = temp.replace('1', '*')
        temp = temp.replace('2', 'o')
        print(temp)

    def __newState(self, newState1 ):
        if len(newState1) != self.n:
            print('#ошибка')
            self.__state = int('1' + '0' * self.n)
        else:
            self.__state = int('1' + newState1)

    state = property(lambda x: str(x.__state)[1:], __newState)



lamps=LampRow(6)
lamps.show()
lamps.state = '100120'
print(lamps.state)
lamps.show()
lamps.state = '10101010'
print(lamps.state)
lamps.show()