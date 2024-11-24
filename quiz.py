questions = [  "1. What is the capital of India?\n a. Delhi \t b. Mumbai\n c. Kolkata\t d. Banglore\n",
              "2. What is the currency of USA? \n a. Rupees \t b. Euro\n c. Dollar\t d. Dirham\n",
              "3. Which is the largest country in the world? \n a. USA \t b. Russia\n c. China\t d. India\n",
              "4. Who is the President of India? \n a. Narendra Modi \t b. Amit Shah\n c. Jethalal Gada\t d. Draupadi Murmu\n",
              "5. Which is the largest Ocean? \n a. Indian ocean \t b. Artic ocean\n c. Pacific ocean\t d. Antartica ocean\n",
              "6. Who is known as the father of physics?\n a. Albert Einstein\t b. Aryabhatta\n c. George Washington\t d. Issac Newton\n",
              "7. Which planet is closest to the sun?\n a. Mercury\t b. Mars\n c. Jupiter\t d. Venus\n",
              "8. In which region of India, Dessert is found?\n  a. Maharashtra\t b. Rajasthan\n c. Kerala\t d. Punjab\n",
              "9. How many states are there in India?\n a. 32 \t b. 27 \n c. 28\t d. 36\n",
              "10. Who first invented light?\n a. Issac Newton\t b. Nikola Tesla\n c. Albert Einstein\t d. Thomas Edison\n "]

answers = ['a', 'c', 'b', 'd', 'c', 'd', 'a', 'b', 'c', 'd']
score = 0

for i in range(10):
    print(questions[i])
    answer = input()

    if(answer== answers[i]):
        print("Correct answer! \n Next Question \n")
        score+=1
    
    else:
        print(f"Oops! Wrong answer \n ")
        break


if(score==10):
    print(f"Congratulations you won the game \n Score: {score}/10")
else:
    print(f"Correct answer is {answers[i]} \nYour score is {score} / 10 \nGame Over!")