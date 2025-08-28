#greet the user
print("Hello!I am a bot!What's your name? :")

#get user input
name=input()

#respond to user's name
print(f"Nice to meet you,{name}!")

#ask a question
print("How are you feeling today?(good/bad) :")
mood=input().lower()

#use conditional statements to respond based on input
if mood=="good":
    print("I'm glad to hear that!")
elif mood=="bad":
    print("I'm sorry to hear that.Hope thins get better soon.")

else: print("I see.Sometimes its hard to put feelings into words")

#ask another question
print("Whats your favourite food?")

#input
food=input()

#response
print(f"Oh!I also love {food}")

#question number 3
print("Whats your hobby?")

#input
hobby=input()

#response
print(f"{hobby} is a nice hobby!")

#question number 4
print("What's your favourite subject in school?")

#input
subject=input()

#response
print(f"I hate {subject},but you're a brilliant student!")

#question number 5
print("Who is your favourite teacher?")

#input
teacher=input()

print("Oh nicee!")

#end conversation
print(f"It was nice chatting with you {name}!good byee!")