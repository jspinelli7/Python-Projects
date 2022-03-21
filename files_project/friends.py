# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'


# hint: readlines()

friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends) # making it a set removes duplicates and makes it unordered which allows for intersection
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open("nearby_friends.txt", "w")

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()






""" MY Attempt
file_input = open("people.txt", "r")
people = file_input.readlines()
print(people)

file_input.close()

user_input = input("Enter all friends, each name separated by a space: ")
friend_list = user_input.split(" ")
friend_list = [s + "\n" for s in friend_list]
# print(friend_list)

nearby_list = [name for name in people if name in friend_list]
# print(nearby_list)

file_output = open("nearby_friends.txt", "w")
with file_output as f:
    for item in nearby_list:
        f.write("%s" % item)
file_output.close
"""

