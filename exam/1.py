s=input("enter the roman letter")
sum=0
dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for i in dic:
    if s==i:
        print(dic.get(i))
        break

else :
    if s.endswith("I"):
        for j in s:
            sum+=dic.get(j)
        
        print(sum)
    else :
        for j in s:
            sum+=dic.get(j)
        print(sum-(s.count("I")*2))