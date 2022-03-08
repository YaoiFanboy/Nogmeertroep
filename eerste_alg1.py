import random
NUM_COLOURS = 6
CODE_LENGTH = 4
# combi 111111 tot 6666

candidateSolutions=[[]]
nextGuesses=[[]]
code=[]
currentGuess=[]
responsePegs=[]
won=False
turn=1
def getCombination():
  combinations=[]
  for i in range(1,NUM_COLOURS+1,1):
    for j in range(1,NUM_COLOURS+1,1):
      for k in range(1,NUM_COLOURS+1,1):
        for l in range(1,NUM_COLOURS+1,1):
          combinations.append([i,j,k,l])
  return combinations
def getRandomCode():
    code = []
    mx  = NUM_COLOURS
    mn =1 
    rnd=1
    for i in range(CODE_LENGTH):
      code.append(random.randint(mn, mx))
    return code
def checkCode(guess,code):
  st=""
  new_guess = guess.copy()
  new_code = code.copy()
  for i in range(len(guess)):
    if new_guess[i]==new_code[i]:
      st+="B"
      new_guess[i]= new_guess[i]*-1
      new_code[i] = new_code[i]*-1
  for j in range(len(code)):
    if new_code[j]>0:
      if new_code[j] in new_guess:
        index= new_guess.index(code[j])
        st+="W"
        new_guess[index] = new_guess[index]*-1
  return st
  
def removeCode(comb, code_to_remove):
  if code_to_remove in comb:
    comb.remove(code_to_remove)
  return comb  
def pruneCodes(comb, current_code,response):
  for i in comb:
    if response!=checkCode(current_code,i):
      comb.remove(i)
  return comb

def minmax(comb, candidateSolutions):
  scoreCount={}
  score= []
  nextGuesses = [];
  for i in comb:
    for j in candidateSolutions:
      st = checkCode(i,j)
      if st in scoreCount.keys():
        scoreCount[st]+=1
      else:
        scoreCount[st] = 1
    mx = getMaxScore(scoreCount)
    
    score.append([i, mx])
    scoreCount={}
  
  mn = getMinScore(score)

  for i in score:
    if i[1]==mn:
      nextGuesses.append(i[0])
  return nextGuesses;

def getMaxScore(score):
  mx=0
  for i in score.keys():
    if score[i]>mx:
      mx = score[i]
  return mx
def getMinScore(score):
  mn=9999999
  for i in score:
    if i[1]<mn:
      mn = i[1]
  return mn
def getNextGuess(comb, candidateSolutions, nextGuesses):
  for i in nextGuesses:
    if i in comb:
      if i!=comb[len(comb)-1]:
        return i
    if i in candidateSolutions:
      if i!=candidateSolutions[len(candidateSolutions)-1]:
        return i
  return []
def main():

  turn = 1;
  won = False;
  code = getRandomCode();
  currentGuess = [1, 1, 2, 2]; # 1122

 # 1296 mogelijkheden met huidige code
  combinations = getCombination()
  candidateSolutions=getCombination()

  print( "Code: ", end="")
  for i in code: 
    print(i, end=" ")
  print()

  while (not won):
    # currentGuess telt niet meer mee
    combinations = removeCode(combinations, currentGuess);
    candidateSolutions = removeCode(candidateSolutions, currentGuess);
    # rode en witte pins
    responsePegs = checkCode(currentGuess, code)

    print( "Turn: " , turn )
    print( "Guess: ", end="")
    for i in currentGuess:
      print(i, end=" ")
    print( "= " , responsePegs )

    # If the response is four colored pegs, the game is won
    if responsePegs == "BBBB":
        won = True;
        print( "Congratulations, Game Won!" )
        break

    candidateSolutions = pruneCodes(candidateSolutions, currentGuess, responsePegs)

    # De MinMax
    nextGuesses = minmax(combinations,candidateSolutions)
    # Volgende gok
    currentGuess = getNextGuess(combinations,candidateSolutions,nextGuesses)

    turn+=1
    print("*"*10)
main()