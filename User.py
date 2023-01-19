print("Welcome to Online Quiz")
print("Ready to start")

score = 0
number = 1

userchoice=input("Question 1: find the square of 49? ")
userchoice_int=int(userchoice)
if userchoice_int == 7:
	print("Correct! Good Job")
	score = score + 1

else:
	print("Wrong! Try Again")

userchoice=input("Question 2: find the square root of 121 ? ")
userchoice_int=int(userchoice)
if userchoice_int == 11:
	print("Correct! Good Job")
	score= score + 1

else:
	print("Wrong! Try Again")

userchoice=input("Question 3: what is the square of 8? ")
userchoice_int=int(userchoice)
if userchoice_int == 64:
	print("Correct! Good Job")
	score= score + 1

else:
	print("Wrong! Try Again")

total_mark = (score/number)

print("mark obtained is", total_mark)


#Pseudocode
#Display welcome to online quiz
#Display ready to start
#Initialize score = 0 and  number = 3
#Prompt the user to answer the first question by answering the question
#if usechoice is the same as the answer,display Correct Good job
#if not,print wrong, try again later.
#Do the same for the other two questions
#calculate the total mark: dividing score by number
#print total_mark
