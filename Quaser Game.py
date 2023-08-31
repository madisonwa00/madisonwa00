import random

print("Welcome to Quaser; the galaxy's best of chance!")
start= float(input("Enter the amount of money you want to bet: "))

round = 0
score = 0

while start > float(start*.25) and start <= float(start*2):
    round = round +1
    print(f'Round: ' +str(round))
    print("Option (use the letter) \n"
          "(A) 1 - 8 \n (B) 4 - 7 ")
    option = (input("Choice: "))
    if option == "A":
        option1 = random.randint(1,8)
        score= score + option1
        print("Score: " + str(score))
        print()
    elif option == "B":
        option2 = random.randint(4,7)
        score= score + option2
        print("Score: " + str(score))
        print()
    if round == 5:
            break
if score == 20 or score<20:
    start = start + float(start*.30)
    print("Your current bet is: $ " +str(start))
    print()
elif score>20:
    start = start - float(start*.40)
    print("Your current bet is: $" +str(start))
    print()
