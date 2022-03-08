import random as rand

x=0
codeBreak={}
colors = ["RED", "GREEN", "YELLOW", "BLUE"]
pins={1:"Red",2:"white",3:"No pin"}
colors_map = {1:"RED", 2:"GREEN", 3:"YELLOW", 4:"BLUE"}
num=[1,2,3,4,5,6]
not_include=set()
temp=[]
comp=[]
no=[]

score=1

while x!=1:
    #Speler master code
    print(colors_map)
    code=list(map(int,input("\nVoer de code in: ")))
    if len(code)!=4:
        flag = 0
        for x in code:
            if x > 4 or x < 1:
                flag = 1
 
        if flag == 1:           
        
            print("\tZo werkt dat niet")
            continue
    else:
        x=1
   


for i in range(4):
        rand.shuffle(num)
        comp.append(num[0])
#4 random nummers
print(colors_map)
print("Gok van de computer : ")
print(comp)
x=0
while x!=1:

    print(pins)
    
    #userfeedback
    feed=list(map(int,input("\nGeef feedback : ")))
    if len(feed)!=4:
        flag = 0
        for x in feed:
            if x > 3 or x < 1:
                flag = 1
 
        if flag == 1:           
        
            print("\tZo werkt dat niet")
            continue
    else:
        x=1
#als feedback ==1 dan stored die het in de codebreaker dict
for i in range(len(feed)):
    if feed[i]==1:
        codeBreak.update({i:comp[i]})
    if feed[i]==2:
        temp.append(comp[i])

    elif feed[i]==3:
        if comp[i]  in no:
            break
        else:

            no.append(comp[i])
            num.remove(comp[i])

while score<=10:
    print("De computer is op "+str(score))

    if len(codeBreak.keys())<1:
        temp.clear()
        comp.clear()
        for i in range(4):
            rand.shuffle(num)
            comp.append(num[0])
    else:
        num=num+temp
        temp.clear()
        comp.clear()
        for i in range(4):
            if i in codeBreak.keys():
                comp.append(codeBreak[i])
            else:
                rand.shuffle(num)
                comp.append(num[0])

        
    print("\n\n")
    print(colors_map)
    print("De computer koos voor : ")
    print(comp)
    x=0

    while x!=1:

        print(pins)
        feed=list(map(int,input("\nVoer de feedback in : ")))
        if len(feed)!=4:
            flag = 0
            for x in feed:
                if x > 3 or x < 1:
                    flag = 1
    
            if flag == 1:           
            
                print("\tSlechte feedback")
                continue
        else:
            x=1
    
        #comp updaten
    for i in range(len(feed)):
        if feed[i]==1:
                codeBreak.update({i:comp[i]})
        if feed[i]==2:
            temp.append(comp[i])
        elif feed[i]==3:
            if comp[i]  in no:
                break
            else:
                no.append(comp[i])
                num.remove(comp[i])
    print(codeBreak)
    if len(codeBreak.keys())==4:
        print("Computer Won")
        print("Je gekozen code is :")
        for i in sorted (codeBreak.keys()) :
            print(codeBreak[i], end = " ")
        break
    else:
        score=score+1



