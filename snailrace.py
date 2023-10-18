import random,sys,time
#constants
MAX_NUM_SNAILS=8
MAX_NAME_LENGTH=20
FINISH_LINE=40
print("""This is just
              a
        Snail game""")

# Ask how many snails to race.
print('Enter a number of snails racing between 2 and {}.'.format(MAX_NUM_SNAILS))
while True:  # keep asking untill the player enters a number
    response=input('>')
    if response.isdecimal():
        num_snails_racing=int(response)
        if 1< num_snails_racing<= MAX_NUM_SNAILS:
            break

# Enter name of each snail.
snailNames = []
for i in range(1, num_snails_racing +1):
    while True:
        print('Enter snail #' + str(i) + "'s name:")
        name=input('>')
        if len(name)==0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used')
        else:
            break # if names entered are acceptable.
    snailNames.append(name)

#Display each snail at the start of the line.
print('\n'*40)
print('START' + (''*(FINISH_LINE -len('START')) + 'FINISH'))
print('|' + (''*(FINISH_LINE- len('|')) + '|'))

snailProgress={}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName]=0

time.sleep(1.5)  # The pause right before the race starts.

while True:  # Main program loop
    # Pick random snail to move forward
    for i in range(random.randint(1, num_snails_racing //2)):
        random_snailName=random.choice(snailNames)
        snailProgress[random_snailName] +=1
        #check if a snail has reached the finish line.
        if snailProgress[random_snailName]==FINISH_LINE:
            print(random_snailName, 'has won!')
            sys.exit()

time.sleep(0.5)
print('\n'*40)

# Display the start and finish line.
print('START' + (''*(FINISH_LINE-len('START')) + 'FINISH'))
print('|' + ('' * (FINISH_LINE-1) + '|'))

# Display the snails(with nametags)
for snailName in snailNames:
    spaces= snailProgress[snailName]
    print(('' * spaces) + snailName[:MAX_NAME_LENGTH])
    print(('.' * snailProgress[snailName]) + '@v')

# Finished