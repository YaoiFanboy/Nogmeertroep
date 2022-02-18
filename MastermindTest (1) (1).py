from doctest import master
import random


#keuze Code maker of code breker
def choice():
    MS=(input('Wil je als code maker of breker spelen? M/B:\n').upper())
    if MS=='B':
        Main_speler()
    
#speler is code bedenker
def Masterscode():
    global MasterCode
    MasterCode=(input('voer de code in, je kunt kiezen uit blauw, rood, groen en geel:\n').upper())
    MasterCode
    MasterCode=MasterCode.split()
    print(MasterCode)


#computer maakt code
def ComputerCode():
    global MasterCode
    global computermastercode
    computermastercode=[]
    random.randrange(1,4)

    for i in range(4):
     computermastercode.append(random.randrange(1,4))
    for j, n in enumerate(computermastercode):
        if n ==1:
            computermastercode[j]='BLAUW'
        if n ==2:
            computermastercode[j]='ROOD'
        if n ==3:
            computermastercode[j]='GROEN'
        if n ==4:
            computermastercode[j]='GEEL'
    MasterCode=computermastercode
    return computermastercode
        
#speler raadcode
def Usercode():
    global UserCode
    UserCode=(input('probeer de code te raden, je kunt kiezen uit groen blauw rood en geel.:\n').upper())
    UserCode
    UserCode=UserCode.split()
    return UserCode

#computer geeft feedback
def Feedback():
    global red
    temp_ans = MasterCode[:]
    pegs = 0
    for i in UserCode:
        if i in temp_ans:
            temp_ans.remove(i)
            pegs += 1
    white=pegs
    red=sum([MasterCode[i] == UserCode[i] for i in range(len(MasterCode))])
    white -= red
    print('het aantal rode pins zijn:',red)
    print('het aantal witte pins zijn:',white)

#hoofd programma van de spelers/code brekers kant
def Main_speler():
    while True:
        Round=1
        ComputerCode()
        while True:
            Usercode()
            Feedback()
            Round +=1
            if red==4:
                print('Geraden in:',(Round-1), 'Nog een keer spelen? Y/N:\n')
                JN=(input().upper())
                if JN=='Y':
                    break
                if JN=='N':
                    exit()
            print('je zit op ronde:',Round,'van de 10')
            if Round==11:
                YN=(input('je rondes zijn voorbij! Nog een keer spelen? Y/N:\n').upper())
                if YN=='Y':
                    break
                if YN=='N':
                    exit()

if __name__ == '__main__':
    print("Running...")
    choice()
    


