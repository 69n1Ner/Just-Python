from itertools import product
k=0
for w in product(sorted('ПАВСИКЙ'),repeat=6):
    w=''.join(w)
    if 'АА' in w or 'ИИ' in w or "АИ" in w or 'ИА' in w:
        k+=1
        if w=='КАКААА':
            print(k)