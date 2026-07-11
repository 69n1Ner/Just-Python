#
# class Tnode:
#     pass
#
# def node(d,L=None,R=None):
#     newNode=Tnode()
#     newNode.data=d
#     newNode.left=L
#     newNode.right=R
#     return newNode
#
# def makeTree(s):
#     k=lastOp(s)
#     if k <0:
#         Tree= node(s)
#     else:
#         Tree=node(s[k])
#         Tree.left=makeTree(s[:k])
#         Tree.right=makeTree(s[k+1:])
#     return Tree
#
# def calcTree(Tree):
#     if not Tree.left:
#         return int(Tree.data)
#     else:
#         n1=calcTree(Tree.left)
#         n2=calcTree(Tree.right)
#         if Tree.data=='+': res=n1+n2
#         elif Tree.data == '-': res = n1 - n2
#         elif Tree.data == '*': res = n1 * n2
#         else: res=n1//n2
#         return res
#
# def priority(op):
#     if op in '+-': return 1
#     if op in '*/': return 2
#     return 100
#
# def lastOp(s):
#     minPrt=20
#     k=-1
#     for i in range(len(s)):
#         if priority(s[i])<=minPrt:
#             minPrt=priority(s[i])
#             k=i
#     return k
#
# A=input('Введите выражение без скобок: ')
# B=makeTree(A)
# print(calcTree(B))
from datetime import datetime

# inf =3000
# w=[]
#
# f=open('input.txt')
# g=f.readline().strip().split(',')
# N=len(g)
#
# for i in range(N):
#     w.append([inf]*N)
# f=open('input.txt')
# for j in range(N):
#     p=f.readline().strip().split(',')
#     for i in range(N):
#         if p[i] != '-' :
#             w[j][i]=int(p[i])
# selected=[False]*N
# dist=[inf]*N
# start=int(input('Введите номер начальной точки: '))-1
# dist[start]=0
# v=start
# minDist=0
# while minDist<inf:
#     selected[v]=True
#     for j in range(N):
#         if dist[v]+w[v][j]<dist[j]:
#             dist[j]=dist[v]+w[v][j]
#     minDist=1e10
#     for j in range(N):
#         if not selected[j] and dist[j]< minDist:
#             minDist=dist[j]
#             v=j
# v=int(input('Введите номер конечной точки: '))-1
# print('Длина пути: ',dist[v])
# print('Путь в обратном порядке: ')
# print(v+1)
# while v!=start:
#     for i in range(N):
#         if i !=v and dist[i]+w[i][v]==dist[v]:
#             v=i
#             break
#     print(v+1)

# TOKEN = "7590043137:AAHFmqbWG91v_vh4CyaCil3Ld34eCycmB5U"
# CHAT_ID = "1174766740"
#
#
# ps aux | grep Duty_11G_bot.py
#
# pgrep -fl Duty_11G_bot.py

# d={"адын":22}
# d['дыва']=d.get('дыва',0)+1
# print(d)
def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    return f(x+1,y)+f(x+3,y)+f(x*2,y)
print(f(3,9))