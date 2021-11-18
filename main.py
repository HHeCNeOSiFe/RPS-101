from collections import deque
import random
import sys
import time

choice_list_f = ['rock', 'sword', 'whip', 'law', 'gun', 'chain', 'pit', 'quicksand', 'tornado', 'dynamite',
                 'helicopter', 'tank', 'sky', 'nuke', 'laser', 'power', 'medusa', 'lightning', 'electricity', 'heart',
                 'robot', 'math', 'video-game', 'fence', 'devil', 'gold', 'platinum', 'diamond', 'dragon', 'satan',
                 'mountain', 'prayer', 'alien', 'ufo', 'rainbow', 'television', 'water', 'rain', 'beer', 'cup',
                 'bowl', 'guitar', 'planet', 'air', 'toilet', 'film', 'grass', 'moon', 'airplane', 'cloud',
                 'paper', 'book', 'butter', 'church', 'sponge', 'vampire', 'money', 'cross', 'community', 'brain',
                 'cockroach', 'spider', 'fish', 'bird', 'cat', 'wolf', 'duck', 'turnip', 'tree', 'bicycle',
                 'noise', 'car', 'train', 'home', 'man', 'baby', 'woman', 'police', 'princess', 'prince',
                 'queen', 'king', 'monkey', 'vulture', 'porcupine', 'blood', 'snake', 'castle', 'computer', 'peace',
                 'axe', 'cage', 'poison', 'scissors', 'school', 'chainsaw', 'fire', 'camera', 'sun', 'wall',
                 'death'
                 ]  # Choice list for size 101 game; f for 'full'

choice_list_w = []  # Will be made the list of choices for each game size using the above list; w for 'words'

print('Welcome to another thrilling game of RPS!\n'
      'Choose from the original RPS-3, or from any of 5, 7, 9, 11, 15, 25, or 101 choice games!\n'
      'Please enter the number of your choice: ')

game_size = input()
acceptable_game_sizes = [3, 5, 7, 9, 11, 15, 25, 101]
while True:  # Makes sure that the game size chosen is viable.
    try:
        game_size = int(game_size)
        if game_size not in acceptable_game_sizes:
            game_size = input('Please enter a number from the *-choices-* listed above.\n')
            continue
        if game_size == 3:
            for i in [0, 50, 93]:
                choice_list_w.append(choice_list_f[i])
        elif game_size == 5:
            for i in [0, 50, 93, 'spock', 'lizard']:
                choice_list_w.append(choice_list_f[i])
        elif game_size == 7:
            for i in [0, 36, 43, 50, 54, 93, 96]:
                choice_list_w.append(choice_list_f[i])
        elif game_size == 9:
            for i in [0, 4, 36, 43, 50, 54, 74, 93, 96]:
                choice_list_w.append(choice_list_f[i])
        elif game_size == 11:
            for i in [0, 4, 24, 36, 43, 50, 54, 65, 74, 93, 96]:
                choice_list_w.append(choice_list_f[i])
        elif game_size == 15:
            for i in [0, 4, 17, 24, 28, 36, 43, 50, 54, 65, 68, 74, 86, 93, 96]:
                choice_list_w.append(choice_list_f[i])
        elif game_size == 25:
            for i in [0, 4, 9, 13, 17, 24, 28, 32, 36, 40, 43, 47, 50, 54, 65, 60, 68, 74, 76, 82, 86, 90, 93, 96, 98]:
                choice_list_w.append(choice_list_f[i])
        elif game_size == 101:
            choice_list_w = choice_list_f
        break
    except:
        game_size = input('Please enter a *-number-* from the choices listed above.\n')
        continue

enter_your_move_prompt = 'Choose from --\n'  # Creating the list of options from which the player gets to choose.

len_choice_list = [len(x) for x in choice_list_w]
for i in range(game_size):
    if i + 1 < 10:
        ljust_num = max([len_choice_list[j] if j % 5 == i % 5 else 0 for j in range(game_size)]) + 1 + 4
        enter_your_move_prompt += f'(0{i + 1}){choice_list_w[i].capitalize()}'.ljust(ljust_num)  # +1 for a space
    else:
        ljust_num = max([len_choice_list[j] if j % 5 == i % 5 else 0 for j in range(game_size)]) + 1 + 4
        enter_your_move_prompt += f'({i + 1}){choice_list_w[i].capitalize()}'.ljust(ljust_num)   # +4 for the '(##)'
    if (i + 1) % 5 == 0:
        enter_your_move_prompt += '\n'

enter_your_move_prompt += '-- or (0) to quit.'

PC = None  # Player choice
NPC = None  # Non-Player choice (Computer choice, but I wanted an excuse to use PC and NPC as variables)

stats = {'wins': 0,
         'losses': 0,
         'ties': 0
         }

while True:
    print(f"{stats['wins']} Wins, {stats['losses']} Losses, {stats['ties']} Ties")

    while True:  # The player input loop.
        print(f'{enter_your_move_prompt}\nPlease enter the number located next to your choice.')

        PC = input()
        try:    # Makes sure the player's choice is viable.
            PC = int(PC)
            if 0 > PC > 101:
                PC = input('Please enter a number from the *-choices-* listed above.\n')
            elif PC == 0:
                sys.exit()
            break
        except:
            PC = input('Please enter a *-number-* from the choices listed above.')

    los_list = []
    win_list = []
    choice_deq = deque(range(game_size))

    middle_index = len(range(game_size)) // 2

    for i in range(middle_index):  # Creates the win/lose lists to compare with the PC's choice
        if PC == max(choice_deq):
            win_list.append(choice_deq[0])
        else:
            win_list.append(choice_deq[PC])
        choice_deq.rotate(-1)

    choice_deq = deque(range(game_size))

    for i in range(middle_index):
        if PC == min(choice_deq):
            los_list.append(choice_deq[-1])
        else:
            los_list.append(choice_deq[PC - 2])
        choice_deq.rotate(1)

    print(f'{choice_list_w[PC - 1].capitalize()} versus.', end='')  # Display what the player chose,
    time.sleep(0.5)                                                 # with a nice little delay...
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(1)

    random_number = random.randint(1, game_size)                    # ...right before displaying what the computer chose
    NPC = random_number
    print(f'\n{choice_list_w[NPC - 1].capitalize()}!', end='')
    time.sleep(1)
    print()

    if PC == NPC:  # Display and record the win/loss/tie:
        print('You tie!')
        stats['ties'] += 1
    elif NPC in win_list:
        print('You lose!')
        stats['losses'] += 1
    elif NPC in los_list:
        print('You win!')
        stats['wins'] += 1

    time.sleep(1.5)
