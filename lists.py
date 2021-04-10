#3/6/2021
#lists
bicycles=['trek', 'condonable', 'recline', 'specialized']
print(bicycles)
print(bicycles[2].upper())
print(bicycles[-1].upper())
print(bicycles[-4].upper())
msg= f"My first bicycle was a {bicycles[2].upper()}."
print(msg)


odds= [1,3,5,7,9]

# exercises with lists 3-1;3-2; 3-3

friends= ['Zarina','Nilufar', 'Madina', 'Malika', 'Yusuf']
print(friends)
print( f"One of my best friend's name is {friends[3].upper()}.")
print( f"One of my best friend's name is {friends[0].upper()}.")
print(f"One of my best friend's name is {friends[1].upper()}.")
print(f"One of my best friend's name is {friends[2].upper()}.")

# list of my favorite cars
cars=['audi','bmw','nissan','honda','lexus','tesla' ]
print(cars)
msg= f"I would like to own a {cars[4].upper()} car in the future."
print(msg)
print( f"I would like to own a {cars[-1].upper()} car in the future.")
print( f"I would like to own a {cars[-6].upper()} car in the future.")

print(friends)
print(f"frinds_name:{friends}")
print(f"My best friends name  is {friends[2].upper()}")

cars.append('tayota')
print(f"new list of cars:{cars}.")
print(cars)
cars[5]='nexia'
print(f"new list of cars:{cars}.")
# using del for removing
del cars[6]

print(friends)
friends.append('mekhribon')
print(f"new list of friends:{friends}.")
print(f"new list of friends:{friends[-1].upper()}.")


#using remove for deleting elements in the list

friends.remove('mekhribon')
print(friends)
#using pop for deleting elements in the list, it returns the element that popped(removed)

removed_one=friends.pop(4)
print(f"new friends list after popping index 4 {friends}")
print(removed_one)

print(cars)
too_expensive= "bmw"
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive.upper()} is too expensive for me.")

#Exercise
invited_friends=['Azim','Mekhribon','Zarnigor', 'Nasiba']
print(f"Dear my friend {invited_friends[0]}, I am inviting you to my birthday party.")
print(f"Dear my friend {invited_friends[1]}, I am inviting you to my birthday party.")
print(f"Dear my friend {invited_friends[2]}, I am inviting you to my birthday party.")
print(f"Dear my friend {invited_friends[3]}, I am inviting you to my birthday party.")
invited_friends[0]= 'John'
print(f"Dear my friend {invited_friends[0]}, I am inviting you to my birthday party.")
print(f"the list of friends that invited previously:{invited_friends}.")
invited_friends.append('Shakhnoza')
print(f"Dear my friend {invited_friends[-1]}, I am inviting you to my birthday party.")
invited_friends.insert(0,'Patrick')
print(f"Dear my friend {invited_friends[0]}, I am inviting you to my birthday party.")
print(f"New list of invited_friends{invited_friends}")
# exercise with deleting
popped_friends = invited_friends.pop(0)
print(f"I am sorry i cannot invite you, {popped_friends} to my birthday party. ")
popped_friends = invited_friends.pop(1)
print(f"I am sorry i cannot invite you, {popped_friends[1]} to my birthday party. ")
print(popped_friends)
print(f"The list of invited friends:{invited_friends}.")


#sorting the list using sort() function 03/07/2021

print(invited_friends)
print(friends)
friends.sort()
print(friends) # this change will occur permanently if we print the list one more time it returns us alphabetical order
print(friends)
print('Here is the original list of invited friends')
print(invited_friends)
print('\nHere is the sorted list of invited friends')
print(sorted(invited_friends))
print('\nThe original list again')
print(invited_friends)

names=['malika','yusuf','mekhribon','azim']
print(sorted(names))
names.reverse()
print(names)
print(bicycles)

names_size=len(names)
print(f"list_size:{names_size}")
print(f"invited friends list: {len(invited_friends)}")

#homeworks
locations=['queens', 'bronx', 'brooklyn', 'manhattan', 'staten island']
print(f"The original places of the store locations{locations}")
sorted(locations)
print(f"sorted locations{sorted(locations)}")
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
