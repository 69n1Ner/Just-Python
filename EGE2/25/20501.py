# from re import fullmatch
# for i in range(1432,10**10+21424,1432):
#     k=0
#     s='8902001'
#     while k<=10:
#
#         if fullmatch(rf'8902[0-9][0-9]{2**k}',str(i)):
#             print(i,i//1432)
#         k+=21424
answers=[]
for q0 in '0123456789':
    for q1 in '0123456789':
        for amp in [str(2**x) for x in range(20)]:
            s='8902'+q0+q1+amp
            if int(s)%1432==0 and int(s)<=10**10:
                answers.append((int(s), int(s)//1432))

answers=sorted(answers)
for i in range(5):
    print(answers[i][0],answers[i][1])