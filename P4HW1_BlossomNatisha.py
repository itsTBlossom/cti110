#Natisha Blossom
#July 7, 2025
#P4HW1
#This is a program for a user to input grades using a loop, adding the grades to a list in order to determine lowest score, score average, and the letter grade associated with the average.

#Number of grades to be entered
print("How many scores do you want to enter? ")
scores_entered = int(input())

print("")

#Score list being stored
scores_list = []

#Loop for entering scores and invalid score message
for i in range(scores_entered):
    scores = float(input(f"Enter score #{i + 1}: "))
    if 0 <= scores <= 100:
        scores_list.append(scores)
    else:
        print("")
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        scores = float(input(f"Enter score #{i + 1} again: "))
        if 0 <= scores <= 100:
            scores_list.append(scores)

#Drop the lowest score from list
if len(scores_list) >1:
    lowest_score = min(scores_list)
    scores_list.remove(lowest_score)

#Calculate score average
score_avg = sum(scores_list)/len(scores_list)

#Determine letter grade

if score_avg >= 90:
    grade = "A"

elif score_avg >= 80:
     grade = "B"

elif score_avg >= 70:
    grade = "C"

elif score_avg >= 60:
    grade = "D"

else:
    grade = "F"

print("")
print("")

#Results with lowest score, list, score average, and letter grade
print('----------Results----------')
print(f"{'Lowest Score : '}{lowest_score:.1f}")
print(f"{'Modified List : '}{scores_list}")
print(f"{'Scores Average : '}{score_avg:.2f}")
print(f"{'Grade : '}{grade}")
print('---------------------------')
