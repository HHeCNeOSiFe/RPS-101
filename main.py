from collections import deque
import random
import sys
import time

acceptable_game_sizes = [3, 5, 7, 9, 11, 15, 25, 101]

print('Welcome to another thrilling game of RPS!')
print('Choose from the original RPS-3, or from any of 5, 7, 9, 11, 15, or 25 choice games!')
game_size = int(input())

if game_size not in acceptable_game_sizes:
    game_size = int(input())

choice_list_w = open(f'RPS-{game_size}.txt').read().split()
choice_list_n = list(range(1, game_size + 1))
middle_index = len(choice_list_n) // 2

PC = None  # Player-Choice
NPC = None  # Non-Player-Choice (Computer choice, but I wanted an excuse to use PC and NPC as variables)

wins = 0
losses = 0
ties = 0

len_choice_list = [len(x) for x in choice_list_w]

enter_your_move_prompt = 'Choose from --\n'

for i in range(game_size):
    if i + 1 < 10:
        ljust_num = max([len_choice_list[j] if j % 5 == i % 5 else 0 for j in range(game_size)]) + 1 + 4
        enter_your_move_prompt += f'(0{i + 1}){choice_list_w[i].capitalize()}'.ljust(ljust_num)  # +1 for a space
    else:
        ljust_num = max([len_choice_list[j] if j % 5 == i % 5 else 0 for j in range(game_size)]) + 1 + 4
        enter_your_move_prompt += f'({i + 1}){choice_list_w[i].capitalize()}'.ljust(ljust_num)   # +4 for the '(##)'
    if (i + 1) % 5 == 0:
         enter_your_move_prompt += '\n'

enter_your_move_prompt += '-- or (0) to quit. --'

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    while True:  # The player input loop.
        # Print the prompt created earlier

        print(f'Enter your move: \n {enter_your_move_prompt}')

        PC = int(input())
        if PC == 0:
            sys.exit()
        elif PC in choice_list_n:
            break
        else:  # I think I could leave this 'else' out as it goes to the print on the next line either way.
            print(f'Type one of [insert list code here] or q.')

    # Make winning and losing lists to compare the PC to:
    los_list = []
    win_list = []

    choice_deq = deque(choice_list_n)
    for n in range(1):
        for i in range(middle_index):
            if PC == max(choice_deq):
                win_list.append(choice_deq[0])
            else:
                win_list.append(choice_deq[PC])
            choice_deq.rotate(-1)

        choice_deq = deque(choice_list_n)

        for i in range(middle_index):
            if PC == min(choice_deq):
                los_list.append(choice_deq[-1])
            else:
                los_list.append(choice_deq[PC - 2])
            choice_deq.rotate(1)

    # Display what the player chose:
    print(f'{choice_list_w[PC - 1].capitalize()} versus...')
    time.sleep(1.75)

    # Display what the computer chose:
    random_number = random.randint(1, game_size)
    NPC = random_number
    print(f'{choice_list_w[NPC - 1].capitalize()}!')
    time.sleep(1)

    # Display and record the win/loss/tie:
    if PC == NPC:
        print('It\'s a tie!')
        ties += 1
    elif NPC in win_list:
        print('You lose!')
        losses += 1
    elif NPC in los_list:
        print('You win!')
        wins += 1

    time.sleep(2.5)
