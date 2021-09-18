secret_no = 9
while True:
    try:
        guess=int(input("your guess :"))
        if guess==secret_no:
            print("correcttttt!")
            break
    except ValueError:
        print("please enter a digit----")    