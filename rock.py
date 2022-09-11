from random import randint


# def choice():
#     x = input(
#         'Please enter "Rock", "Paper", or "Scissors". Enter "Quit" to quit. ')
#     return word.title()


# print(f"Player's choice is {choice()}")
# x = choice()


# def comp():
#     words = ['Rock', 'Paper', 'Scissors']
#     spot = (randint(0, (len(words)-1)))
#     return words[spot]


# print(f"Computer's choice is {comp()}")

# y = comp()


# def results():
#     while True:
#         words = ['Rock', 'Paper', 'Scissors']
#         b = (randint(0, (len(words)-1)))
#         y = words[b]
#         x = input(
#             'Please enter "Rock", "Paper", or "Scissors". Enter "Quit" to quit. ')
#         while True:

#             a = x.title()

#             print(f"Computer's choice is {y}")
#             print(f"Player's choice is {a}")
#             if a == 'Quit':
#                 break
#             elif a == y:
#                 return "Tie Game"
#             elif a == 'Rock' and y == 'Paper':
#                 return "You Lose"
#             elif a == 'Paper' and y == 'Scissors':
#                 return "You Lose"
#             elif a == 'Scissors' and y == 'Rock':
#                 return "You Lose"

#             elif a == 'Rock' and y == 'Scissors':
#                 return "You Win"

#             elif a == 'Paper' and y == 'Rock':
#                 return "You Win"

#             elif a == 'Scissors' and y == 'Paper':
#                 return "You Win"
#             if a == 'Quit':
#                 break

#             else:
#                 return "That is not a valid entry, try again!"


# print(results())
while True:
    words = ['Rock', 'Paper', 'Scissors']
    b = (randint(0, (len(words)-1)))
    y = words[b]
    x = input(
        'Please enter "Rock", "Paper", or "Scissors". Enter "Quit" to quit. ')

    a = x.title()

    print(f"Computer's choice is {y}")
    print(f"Player's choice is {a}")
    if a == 'Quit':
        break
    elif a == y:
        print('Tie Game')
    elif a == 'Rock' and y == 'Paper':

        print('You Lose.')

    elif a == 'Paper' and y == 'Scissors':
        print('You Lose.')
    elif a == 'Scissors' and y == 'Rock':
        print('You Lose.')

    elif a == 'Rock' and y == 'Scissors':
        print("You Win")
    elif a == 'Paper' and y == 'Rock':
        print("You Win")
    elif a == 'Scissors' and y == 'Paper':
        print("You Win")
    # else:
    #     print("That is not a valid entry, try again!")
print('Thank you for playing!')
