#This is the most basic assignment of day 1, that takes user mark as user input and prints the output.
x = int(input("Enter your mark here: "))
if x <= 100:
        if x < 32:
                print("Oops!! We're sorry to say that you failed.")
        elif x == 32:
                print("You're just pass !")
        elif x > 32 and x <= 60:
                print("Congrats, You're pass!!")
        elif x > 60 and x <=100:
                print("Wow, You're excellent !!!")
        else:
                print("The mark is not valid !")
else:
        print("Your mark cannot be more than 100.")
