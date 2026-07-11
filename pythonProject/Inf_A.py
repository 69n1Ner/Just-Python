from animals_A import *
p = Dog('Шарик',5)
p.gettingOlder()
print(p.name + ':',p.age,"лет")
pets = [Cat('Мурка',3),p]
for p in pets:
    p.say()