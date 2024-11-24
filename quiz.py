print("Welcome to Python Quiz Game")
print("You will be presented with questions and four options each.")
print("Type the letter of the option you think is correct.")
print("Let's get started!\n\n")

def Gameover():
    print("Game Over!")

questions = [  "1. What is the capital of India?\n a. Delhi \t b. Mumbai\n c. Kolkata\t d. Banglore\n",
              "2. What is the currency of USA? \n a. Rupees \t b. Euro\n c. Dollar\t d. Dirham\n",
              "3. Which is the largest country in the world? \n a. USA \t b. Russia\n c. China\t d. India\n",
              "4. Who is the President of India? \n a. Narendra Modi \t b. Amit Shah\n c. Jethalal Gada\t d. Draupadi Murmu\n",
              "5. Which is the largest Ocean? \n a. Indian ocean \t b. Artic ocean\n c. Pacific ocean\t d. Antartica ocean\n",
              "6. Who is known as the father of physics?\n a. Albert Einstein\t b. Aryabhatta\n c. George Washington\t d. Issac Newton\n",
              "7. Which planet is closest to the sun?\n a. Mercury\t b. Mars\n c. Jupiter\t d. Venus\n",
              "8. In which region of India, Dessert is found?\n a. Maharashtra\t b. Rajasthan\n c. Kerala\t d. Punjab\n",
              "9. How many states are there in India?\n a. 32 \t b. 27 \n c. 28\t d. 36\n",
              "10. Who first invented light?\n a. Issac Newton\t b. Nikola Tesla\n c. Albert Einstein\t d. Thomas Edison\n "]

answers = ['a', 'c', 'b', 'd', 'c', 'd', 'a', 'b', 'c', 'd']
score = 0

for i in range(10):
    print(questions[i])
    answer = input("Your answer (a/b/c/d): ").lower()

    if(answer== answers[i]):
        print("\nCorrect answer! \nNext Question \n")
        score+=1
    
    else:
        print(f"\nOops! Wrong answer \tCorrect answer is {answers[i]}")
        break


if(score==10):
    print(f"Excellent! You got all questions right!\nCongratulations you won the game \nScore: {score}/{len(questions)}")
    Gameover()
elif(score>= len(questions)/2):
    print(f"Good job! You did well. Score: {score}/{len(questions)}")
    Gameover()
else:
    print(f"Your score is {score}/{len(questions)} \nBetter luck Next time")
    Gameover()