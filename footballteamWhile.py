football_team = []
#append values
for i in range(11):
    new = input("add a new name to the list: ")
    football_team.append(new)
repeat = "Y"
while repeat == "Y":
    #edit an item
    print(football_team)
    #identify the range of indexes
    final_index = len(football_team) - 1
    print("You can print any name from the list. Index number go from 0")
    i = input("Which name do you want to change?")
    i = int(i)
    #validation with while loop
    while i >= len(football_team):
        i = int(input("Enter correct number: "))
    football_team[i] = input("Enter a new name: ")
    print(football_list)

    #delete an item
    print("You can delete any name rom the list. Index numbers go from 0")
    i = input("Which name do you want to delete?")
    i = int(i)
    #validation
    while i >= len(football_team):
        i = int(input("Enter correct number: "))
    del football_team[i]
    print(football_team)
    repeat = input("do you want to edit or delete name?(Y/N) ")