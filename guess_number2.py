import random
the_number=random.randint(1,100)
while True :
    input_number=input()
    if input_number.isnumeric():
        guess_number=int(input_number)
        Judgement_input()
    else:
        print("You must type an integer!")
    


    def Judgement_input():
        if the_number < guess_number:
            print("It's too large!")
        elif the_number > guess_number:
            print("It's too small!")
        elif the_number == guess_number:
            print("Congratulation!")
            quit(0)
