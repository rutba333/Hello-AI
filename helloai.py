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

#end conversation
print(f"It was nice chatting with you {name}!good byee!")

