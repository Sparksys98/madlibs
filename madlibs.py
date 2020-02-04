def main():
	# write your code here
	print("Mad libs where libs get mad.")
	print("Start below:")
	print(" ")
	time=input("Enter a number from 1 to 12: ")
	items=input("Enter a noun (plural): ")
	name=input("Enter a name: ").capitalize()
	scream=input("Enter any sentnce: ").upper()
	action=input("Enter any action: ")

	print("The story goes...")
	print(" ")


	result=('''It was {} o'clock when I heard a knock at the door.
	I opened the door and there was a box full of {} with a note saying "From Mr. {}."
	Just as I closed the door I heard a scream "{}."
	I froze in place and all I could do was {}.''').format(time,items,name,scream,action)
	print(result)
main()
