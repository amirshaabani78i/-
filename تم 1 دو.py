menu_koli = input()
h = menu_koli.replace(' ', ',')
m = h.split(',')
dic_aval = dict(zip(m[0::2], map(float, m[1::2])))

from collections import defaultdict
l1=[]
l2=[]
while True:
    f=input()
    if f.lower()=="end":
        break

    p=f.split(",")
    for z in p:
        o=z.split(" ")
        l1.extend((o[0::2]))
        l2.extend(map(float,o[1::2]))
        
dic_dovom = defaultdict(float)

for key,value in zip(l1,l2):
      dic_dovom[key] += value

for e in dic_aval.keys():
    if e in dic_dovom.keys():
        print(e ,round(dic_aval[e]*dic_dovom[e],2) )
    else:
        print(e,float(0*1))


