import random 

while True:
    secret_number = random.randint(1,5)

    attempts = 5

    while True:
       guess = int(input("Entre the number : "))

       attempts = attempts - 1
       print("attempts left: " ,attempts)

       if guess == secret_number:
          print("you won !")
          break 

       elif guess > secret_number:
           print("Too high !")

       else:
            print("Too low")

       if attempts == 0:
            print("game over")
            break

    answer = input("If you want to continue press c: ")

    if answer == "c":
        continue
    else:
        print("Thankyou for playing")
        break

