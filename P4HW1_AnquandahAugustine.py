#CTI-110
#P4HW1- Score List
#Anquandah Augustine
#4/24/2023




#taking numofscores as input from user
numofscores=int(input(" How many scores do you want to enter? : "))
print()
#creating an empty list to store scores
scoreslist=[]

#for loop to take scores as inputs
for i in range(1,numofscores+1):
    
    #while loop to take input until user enters correct input
    while True:
        try:
            #taking score as input from user
            score=int(input("Enter score {}: ".format(i)))
            
            #checking if score is between 0 and 100
            if score>=0 and score<=100:
               
                #if yes, then appends to list
                scoreslist.append(score)
                break
            #if not, then prints this and asks for input again
           
            else:
                print()
                print("INVALID Score entered!!!!") 
                print("Score should be between 0 and 100")
        except:
            continue

print()


print("------------------Results--------------------")

#printing lowest score entered
lowestscore=min(scoreslist)
print("\nLowest score : %.1f"%(lowestscore))

#rprinting modified list after dropping lowest score
scoreslist.remove(lowestscore)
print("\nModified List: {}".format(scoreslist))

#printing average of modified scoreslist
avgofscoreslist=sum(scoreslist)/len(scoreslist)
print("\nScores Average: %.2f"%(avgofscoreslist))

#printing letter grade

if avgofscoreslist>90 and avgofscoreslist<=100:
    print("Grade: A")
elif avgofscoreslist>80 and avgofscoreslist<=90:
    print("Grade: B") 
elif avgofscoreslist>70 and avgofscoreslist<=80:
    print("Grade: C")
elif avgofscoreslist>60 and avgofscoreslist>=70:
    print("Grade: D")
else:
    print("Grade: E")
