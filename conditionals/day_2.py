#  SET is it raining = INPUT "Is it raining?"
# IF is_it_raining is "yes"
#   THEN PRINT "You shoud take the car"
#ELSE
#   IF distance < 5
#       THEN PRINT "You should walk"
#   ELSE 
#       THEN PRINT "You should get the bus"

distance = 4
is_it_raining = input("Is it raining? ")

if is_it_raining == "yes":
    print("You should take the car")
else:
    if distance < 5:
        print("Walk, ya lazy prick")
    else:
        print("You should get the bus")

