
#halve donald Knuth algoritme
import random as rand

colors = ["RED", "GREEN", "YELLOW", "BLUE"]
pins={1:"Red",2:"white",3:"No pin"}
colors_map = {1:"RED", 2:"GREEN", 3:"YELLOW", 4:"BLUE",}
a_list=[1,2,3,4]
all_combinations = []
#vul de lijst met alle combinaties
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                all_combinations.append([a_list[i],a_list[j],a_list[k],a_list[l]])
res=[]

#dubbele eruit halen
for i in all_combinations:
    if i not in res:
        res.append(i)

dic={}
#speler master code invoeren
code=list(map(int,input("\nVoer de code in : ")))
if len(code)!=4:
        flag = 0
        for x in code:
            if x > 4 or x < 1:
                flag = 1
 
        if flag == 1:           
        
            print("\t Geen goeie input")
            
for i in range(10):
    codeBreak={}
    print("De computer is op beurt:",i)
    
    
    rand.shuffle(res)
    comp=res[0]
    print("De Computer gokte: ",comp)
    #computer gokt iets
    x=0
    while x!=1:

        print(pins)
        #feedback van de speler
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
    temp={}
    new=[]
    h=[]
    
    for i in range(len(feed)):
        #verwijderd alles dat geen rode pin had 
        if feed[i]==1:
            codeBreak.update({i:comp[i]})
            for element in res:
                for keys in codeBreak:
                    j=element[keys]
                    k=codeBreak[keys]
                    if j!=k:
                        new.append(element)
     
     # verwijderd alles met 2 op de index voorkoming van dubbele
        if feed[i]==2:
            for element in res:
                for keys in temp:
                    j=element[keys]
                    k=temp[keys]
                    if j==k:
                        h.append(element)          
    
    res= [x for x in res if x not in new]
    res= [x for x in res if x not in h]
    if len(res)==1:
        print("computer heeft gewonnen : ",res[0])
        break
    
    
    

                


    

