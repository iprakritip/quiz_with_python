print("Welcome to the Quiz!!")

playing = input("Are you ready to play? ")

if playing.lower()!='Yes'.lower():
    print("Sad to see you go :(")
    quit();

print("Well then, buckle up !!")

score=0

answer = input("What's the full form of CPU? ")

if answer.lower()=='central processing unit'.lower():
    print('Correct!')
    score+=1
else:
    print("Oops!! Wrong answer.")

answer = input("What does .py refer to in a python file? ")

if answer.lower()=='python'.lower():
    print('Correct!')
    score+=1
else:
    print("Oops!! Wrong answer.")


answer = input("What is the capital of Turkey? ")

if answer.lower()=='Ankara'.lower():
    print('Correct!')
    score+=1
else:
    print("Oops!! Wrong answer.")


answer = input("What is the full form of WHO? ")

if answer.lower()=='world health organization'.lower():
    print('Correct!')
    score+=1
else:
    print("Oops!! Wrong answer.")


answer = input("How many bones do humans have? ")

if int(answer)==206:
    print('Correct!')
    score+=1
else:
    print("Oops!! Wrong answer.")


print("You got "+ str(score) +" questions correct.")
print("You got "+ str((score/5)*100) +" %.")