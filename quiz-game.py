#answer the full form.
print("Welcome to the game of quiz!")

playing = input("Do you want to move forward/play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!, you got a point.')
    score += 1
else:
    print("😳 Incorrect!, that is the easiest question put some effort in answering.")
   
 
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!, you got a point.')
    score += 1
else:
    print("Incorrect!,😟")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!,😟")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!,😟")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
