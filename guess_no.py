import random

x=random.randint(1,20)
attempt=0
won = False

print("Note:5 Guess and game's over.")

while attempt < 5:
	guess=int(input("Guess the number:"))
	attempt += 1
	
	
	
	if guess == x:
		print(f"You guessed it in {attempt} attempts")
		won=True
		break

	elif guess>x:
		print("Nope too high!")
	else:
		print("Nah too low!")
if not won:
		print(f"Game over ,the number was{x}")