import random


def add_asking(n):
    global list
    if not n.isspace:
        print('Do not add space ! since this is user name')
        exit()
    else:
        if n in list:
            uniq_id = random.randint(52, 999)
            n = uniq_id
            list.append(n)

            print(f'You Have been assigned with a unique ID - {uniq_id}')
            print('THIS IS THE LIST OF NUMBERS = ', list)
            exit()
        list.append(n)
        print(n, 'Has Been Added Successfull')
        print('THIS IS THE LIST OF NUMBERS = ', list)
        


list = ['Bhavik', 'Lalit', 'Vivek', 'Kishori', 'Jayshree']

for all in list:
    if 'i' in all or 'i' not in all:
        print(all, end=' ')
    print()
    
asking = input('What name would you like to suggest - ')
add_asking(asking.capitalize())
