from random import choice


print('Enter the number of friends joining (including you):')
friends_num = int(input())
if friends_num <= 0:
    print("\nNo one is joining for the party")
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    friends_list = {input(): 0 for _ in range(friends_num)}
    print('\nEnter the total bill value:')
    total_bill = int(input())
    lucky_winner = None
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if input() == 'Yes':
        lucky_winner = choice(list(friends_list.keys()))
        print(f"\n{lucky_winner} is the lucky one!")
        friends_num -= 1  # not a friend anymore :P
    else:
        print("No one is going to be lucky.")
    bill_share = round(total_bill/friends_num, 2)
    for friend in friends_list:
        friends_list[friend] = bill_share
    if lucky_winner is not None:
        friends_list[str(lucky_winner)] = 0
    print("\n", friends_list, sep='')
