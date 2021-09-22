name = input("Please Enter your name, Sir/Ma'am : ")
print("Welcome to Computer Quiz Game,",name)
print("\n")
print("We hope that you will enjoy this game ")
print("\n")
playing = input("Do you want to play, Sir/Ma'am ? ")
if playing.lower()!="yes":
     quit()


print("Okay! Let's play :) ")
score=0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
     print("Correct!")
     score+=1
else:
     print("Incorrect!")

print("\n")


answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
     print("Correct!")
     score+=1
else:
     print("Incorrect!")

print("\n")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
     print("Correct!")
     score+=1
else:
     print("Incorrect!")
print("\n")

#Fourth Question
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply" or answer.lower() == "public sector unit":
     print("Correct!")
     score+=1
else:
     print("Incorrect!")

print("\n")
#Fifth 
answer = input("What does IB stand for? ").lower()
if answer == "intelligence bureau":
     print("Correct!")
     score+=1
else:
     print("Incorrect!")




print("You've got "+ str(score)+" questions correct!")
print("You've got "+ str((score/5) * 100)+"%.")




print("Thanks for playing this game")
print("Have a nice day! ")