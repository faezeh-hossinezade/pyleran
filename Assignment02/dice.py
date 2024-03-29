import random

print("Start 🎲 :")
txt = input("Turn Dic... : ")

while(txt!="exit"):
    dic_num = random.randint(1,6)
    
    if dic_num == 6:
        print("current 🎲 for 6: ",dic_num)
        print("🎉🎉🎉 P R I Z E 🎉🎉🎉")
        txt = input("Start Dic Again... : ")
    else:
        print("current 🎲 : ",dic_num)