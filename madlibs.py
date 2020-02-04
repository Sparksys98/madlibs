def main():
	# write your code here
	print("Mad libs where libs get mad.")
	print("Start below:")
	print("")
	time=raw_input("Enter a number from 1 to 12: ")
	items=raw_input("Enter a noun (plural): ")
	name=raw_input("Enter a name: ").capitalize()
	scream=raw_input("Enter any sentnce: ").upper()
	action=raw_input("shake my head: ")

	print("The story goes...")

	print('''It was %s o'clock when I heard a knock at the door.
	I opened the door and there was a box full of %s with a note saying "From Mr. %s."
	Just as I closed the door I heard a scream "%s."
	I froze in place and all I could do was %s.''') % (time,items,name,scream,action)
main()
