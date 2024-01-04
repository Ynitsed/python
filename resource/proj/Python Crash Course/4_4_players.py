# Page 65 Slicing a list
print("\n------------------------------------------\n")
players = ['charles', 'martina', 'michael', 'florence', 'eli']


print(players[0:3]) #['charles', 'martina', 'michael']
print("\n------------------------------------------\n")

print(players[1:4]) #['martina', 'michael', 'florence']
print("\n------------------------------------------\n")

print(players[:4])  #['charles', 'martina', 'michael', 'florence']
print("\n------------------------------------------\n")

print(players[2:])  #['michael', 'florence', 'eli']
print("\n------------------------------------------\n")

print(players[-3:]) #['michael', 'florence', 'eli'] This prints the names of the last three players and would continue to work as the list of players changes in size.
print("\n------------------------------------------\n")

#Looping Through a Slice
for player in players[:3]:
    print(player.title())
print("\n------------------------------------------\n")


