#exception handling:
while True:
    try:
        num=int(input("enter the value:"))
        if num == 1:
          print("greece")
          break
        elif num == 2:
          print("france")
          break
        elif num == 3:
          print("mal")
          break
        elif num == 4:
          print("ita")
          break
        elif num == 5:
          print("florida")
          break

    except ValueError:
        print("please type a no. : ")
    except:
        print("unknown error occured.")
print("thank you & bye")            
