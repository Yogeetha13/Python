import random
roll_again = "y"

Roll = random.randint(1, 6)
if Roll == 1:
    print("number is",Roll)
    elif Roll == 2:
         print("number is",Roll)
    elif Roll == 3:
	 print("number is",Roll)
    elif Roll == 4:
    	 print("number is",Roll)
    elif Roll == 5:
         print("number is",Roll)
    else:
         print("number is",Roll)

while roll_again == "y":
	print "Rolling the dices..."
        print "The values are...."
	print random.randint(1, 6)

	roll_again = raw_input("Roll the dices again?")

