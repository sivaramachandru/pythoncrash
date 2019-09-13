from random import randint
num_games = int(input("Enter how many games you want to play"))
print(f"Alright let us play {num_games} games")
guessnumber = randint(1,25)
counter = 0
for x  in range(num_games):
	print(f" Game {x}  :")
	y = int(input("\nenter random number 1 - 25"))
	if y > 25 or y <1:
		print("\n Enter number is not in range")
		y = int(input("\nenter random number 1 - 25"))
	counter += 1


	if y == guessnumber:
		print(f"\nYou guess number right and you took {counter}")
		break
	else:
		print("\nNot right, try again")