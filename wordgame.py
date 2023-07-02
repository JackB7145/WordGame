import random
import time
import copy
infile = open("dictionary.txt", "r")
dictionary = infile.read().split("\n")

#Defining the recursive function
def makeWord(currentX, currentY, grid, charactersLeft, word, value):

    #Base case and a word is found
    if word in dictionary and not(word in wordsfound) and len(word) > 4:
        wordsfound.append(word)
        return [grid, word]
    
    elif charactersLeft == 0:
        return 1
    else:
 
        character = grid[currentY][currentX]

        grid[currentY][currentX] = value+1
        
        counter = 0
        while True:
            try:
                counter += 1
                if counter > 10:
                    return 2
                x = random.randint(-1, 1)
                y = random.randint(-1, 1)
                if type(grid[currentY + y][currentX + x]) is str and currentY + y != -1 and currentX + x != -1:
                    break
            except:
                continue
            
        return makeWord(currentX + x, currentY + y, grid, charactersLeft-1, word+character, value+1)

ar = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
wordsfound = []
print("\nEnter in the board!\n")

for y in range(len(ar)):
    for x in range(len(ar[0])):
        ar[y][x] = input("Enter your character: ").upper().replace(" ", "")

while True:
    wordLength = 8
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    answer = makeWord(x, y, copy.deepcopy(ar), wordLength, "", 0)
    if type(answer) is list:
        for x in answer[0]:
            print(x)
        print("\n", answer[1])
        time.sleep(1.5)
        
