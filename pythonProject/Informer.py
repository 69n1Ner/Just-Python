# s = input('Число :')
# a = []
# while len(s) > 0 :
#     w =  s[-3 :]
#     s =  s[ :-3]
#     x =  int(w)
#     a.append(x)
# print('Ответ',a)
from cmath import phase
from os.path import split
from pprint import pprint

from select import select

# A  =  [1]
# d  =  1000000
#
# for k in range(2, 101) :
#     r  =  0
#     for i in range(len(A)) :
#         s  =  A[i] * k + r
#         A[i]  =  s % d
#         r  =  s // d
#     if r > 0 :
#         A.append(r)
#
# h  =  len(A) - 1
# j = 0
# j+ = len(str(A[h]))
# print(A[h], end = '')
# for i in range(h - 1, -1, -1) :
#     e = f'{A[i] :06d}'
#     j+ = len(e)
#     print(f'{A[i] :06d}', end = '')
# print()
# print(j)

# s = input('Число :')
# a = []
# while len(s) > 0 :
#     w =  s[-6 :]
#     s =  s[ :-6]
#     x =  int(w)
#     a.append(x)
# print('Ответ',a)


# def part_long_number_str(s) :
#     a  =  []
#     while len(s) > 0 :
#         w  =  s[-6 :]
#         s  =  s[ :-6]
#         x  =  int(w)
#         a.append(x)
#     return a
#
# X = input('Число X :',)
# Y = input('Число Y :',)
# X = part_long_number_str(X)
# Y = part_long_number_str(Y)
#
# A  =  []
# d  =  1000000
#
# m  =  max(len(X), len(Y))
# X.extend([0] * (m - len(X)))
# Y.extend([0] * (m - len(Y)))
#
# for i in range(m) :
#     r  =  0
#     s = X[i]+Y[i]
#     A.append(s)
#     r = A[i]//d
#     A[i] % =  d
#     if r>0 :
#         A.append(r)
#
# h  =  len(A) - 1
# print(A[h], end = '')
# for i in range(h - 1, -1, -1) :
#     print(f'{A[i] :06d}', end = '')


# def show_long_num_str(s) :
#     a  =  []
#     while len(s) > 0 :
#         w  =  s[-6 :]
#         s  =  s[ :-6]
#         x  =  int(w)
#         a.append(x)
#         h  =  len(a) - 1
#     print(a[h], end = '')
#     for i in range(h - 1, -1, -1) :
#         print(f'{a[i] :06d}', end = '')
# k = show_long_num_str(input())



# def input_long_num_from_txt(fname) :
#     a  =  []
#     f  =  open(fname)
#     g  =  str(f.readline())
#     while len(g) > 0 :
#         w  =  g[-6 :]
#         g  =  g[ :-6]
#         x  =  int(w)
#         a.append(x)
#         h  =  len(a) - 1
#     print(a[h], end = '')
#     for i in range(h - 1, -1, -1) :
#         print(f'{a[i] :06d}', end = '')
# input_long_num_from_txt('in.txt')



       #Cумматор длинных чисел (не вводить отрицательные )
# def input_long_num_from_txt(fname) :     #берет длинное число в виде сторки из файла и преобразует в длинное число в виде списка (удобно для счета дальнейшего)
#     a  =  []
#     f  =  open(fname)
#     g  =  str(f.readline())
#     if '-' in g :
#         g = g[1 :]
#         while len(g) > 0 :
#             w  =  g[-6 :]
#             g  =  g[ :-6]
#             x  =  int(w)*(-1)
#             a.append(x)
#     else :
#         while len(g) > 0 :
#             w  =  g[-6 :]
#             g  =  g[ :-6]
#             x  =  int(w)
#             a.append(x)
#     return a
#
#
#
# X = input_long_num_from_txt('sum.txt')   #слогаемые
# Y = input_long_num_from_txt('in.txt')
#
# A = []
# d = 1000000
# if '-' in X and len(X)-1>len(Y) and '-' in Y :
#     d  =  -1000000
# elif '-' in Y and len(Y)-1>len(X) and '-' in X :
#     d  =  -1000000
# elif '-' in X and '-' in Y :
#     d  =  -1000000
# elif '-' in Y and len(Y)-1>len(X) :
#     d  =  -1000000
# elif '-' in X and len(X)-1>len(Y) :
#     d  =  -1000000
#
# m  =  max(len(X), len(Y))
# X.extend([0] * (m - len(X)))
# Y.extend([0] * (m - len(Y)))
#
# for i in range(m) :
#     s = X[i]+Y[i]
#     print('X',X[i])
#     print('Y',Y[i])
#     A.append(s)
#     print(A)
#     A[i] % =  d
#     print('last',A)
# h  =  len(A) - 1
# print(A[h], end = '')
# for i in range(h - 1, -1, -1) :
#     if A[i]<0 :
#         A[i]* = -1
#     print(f'{A[i] :06d}', end = '')



# D = {}
# F = open('1st.txt','r',encoding = 'utf-8')
# while True :
#     word = F.readline().strip()
#     if not word : break
#     word = word.split()
#     while len(word)>0 :
#         i = word.pop(0)
#         j = word.pop(0)
#         D[i] = D.get(i,j)
# F.close()
#
# A = list(D.items())
# A.sort(key = lambda x :x[0])
#
# F = open('2nd.txt','w')
# for g in A :
#     F.write(f'{g[0]} :{g[1]}\n')
# F.close()
#
# ru_word = input('Слово на русском  : ')
# F = open('2nd.txt')
# while True :
#     look = F.read().strip()
#
#     if ru_word not in look :
#         print('error')
#         break
#     else :
#         print('',F)
#         break




# D = {}         #создание словаря D
# F = open('1st.txt')   #открытие 1-го файла записано в переменную F
# while True :     #цикл, который будет выполняться до тех пор, пока есть строки для чтения
#     check  =  ",. :;!?()'" #создали набор со знаками препинания
#     word = F.readline().strip().lower()  #в переменной word читаем строку из F и удаляем \n
#                                 #теперь еще и делаем все буквы текста маленькими - .lower()
#     if not word : break   #условие, которое заканчивает цикл, если не осталось строк
#     word  =  ''.join([j for j in word if j not in check])  #удаляем все знаки из нашего набора знаков
#     word  =  word.split()  #Разделим те символы, которые получили по словам, т.е. Выше получили только символы
#                         #а здесь разделим эти символы на слова, отделяя их по пробелу
#     D[word] = D.get(word,0)+1  #проверка на то есть ли в словаре слово(добавится 1 к значению)
#                             #если нет слова, то запишет его и в значение добавит 1
# F.close()     #закрывает файл
#
# A = list(D.items())  #словарь D превращаем в список A
# A.sort(key = lambda x : (-x[1], x[0]))#сортируем список А по алгоритму :
#             #сначала сравниваем значения с минусом, а после ключи по алфавиту
#
# F = open('2nd.txt','w')    #открывает файл и разрешает в нем запись в переменную F
# for g in D.items() :     #для каждого элемента g в словаре D выполнить :
#     F.write(f'{g[0]} :{g[1]}\n')   #записать в файл F ключ и значение в формате : ключ :значение

'''
inf  =  3000
w  =  []

f  =  open('input.txt')
g  =  f.readline().strip().split(',')
N  =  len(g)
f.close()

for i in range(N)  :
    w.append([inf]*N)
f  =  open('input.txt')
for j in range(N)  :
    p  =  f.readline().strip().split(',')
    for i in range(N)  :
        if p[i] != '-'  :
            w[j][i]  =  int(p[i])
f.close()

selected  =  [False]*N
dist = [inf]*N
start = int(input('Введите номер начальной точки: '))-1                 #доделать если бы были названия вершин, а не номера
dist[start] = 0
v = start
minDist = 0
while minDist<inf :
    selected[v] = True
    for j in range(N) :
        if dist[v]+w[v][j]<dist[j] :
            dist[j] = dist[v]+w[v][j]
    minDist = 1e10
    for j in range(N) :
        if not selected[j] and dist[j]< minDist :
            minDist = dist[j]
            v = j

v = int(input('Введите номер конечной точки: '))-1
print('Длина пути: ',dist[v])
A = [v+1]
while v!= start :
    for i in range(N) :
        if i != v and dist[i]+w[i][v] == dist[v] :
            v = i
            break
    A.append(v+1)

A = A[::-1]
for l in range(len(A)) :
    if l == len(A)-1 :
        print(A[l])
    else :
        print(A[l],end = '-->')
'''

'''
def F(n):
    if n<2:
        return 1
    if n>=2 and n%3==0:
        return F(n/3)-1
    if n>=2 and n%3!=0:
        return F(n-1)+17
A=0
for i in range(1,1000000000+1):
    if F(i)==43:
        A+=1
    print(F(i))
print(A)
'''





'''
A=0
F=[0]*1_000_000_000_000
for i in range(len(F)):
    if i <2:
        F[i]=1
    if i>=2 and i%3==0:
        F[i]=F[i//3]-1
    if i>=2 and i%3!=0:
        F[i]=F[i-1]+17
    if F[i]==43:
        A+=1
print(A)
'''


# from random import randint
# class Parrot:
#     def __init__(self,phrase0):
#         self.phrase=[phrase0]
#
#     def say(self,n=1):
#         i=randint(1, len(self.phrase))
#         while n>0:
#             print(self.phrase[i-1],end=' ')
#             n-=1
#         print()
#
#     def newText(self,newPhrase):
#         self.phrase=[newPhrase]
#
#     def learn(self,learnPhrase):
#         self.phrase.append(learnPhrase)
#
#
# p=Parrot('Гав')
# p.say()
# p.newText('Мяу')
# p.say(2)
# p.learn('Гав')
# p.say(3)



# class LampRow:
#     def __init__(self,n1):
#         self.n = n1
#         self.__state = int('1' + '0' * self.n)
#
#     def show(self):
#         temp = str(self.__state)[1:]
#         temp = temp.replace('0','-')
#         temp = temp.replace('1', '*')
#         temp = temp.replace('2', 'o')
#         print(temp)
#
#     def __newState(self, newState1 ):
#         if len(newState1) != self.n:
#             print('#ошибка')
#             self.__state = int('1' + '0' * self.n)
#         else:
#             self.__state = int('1' + newState1)
#
#     state = property(lambda x: str(x.__state)[1:], __newState)
#
#
#
# lamps=LampRow(6)
# lamps.show()
# lamps.state = '100120'
# print(lamps.state)
# lamps.show()
# lamps.state = '10101010'
# print(lamps.state)
# lamps.show()


