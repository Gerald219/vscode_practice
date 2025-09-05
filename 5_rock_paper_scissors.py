import random # python random tool

options = ["rock", "paper", "scissors"] # game options

emojis = {"rock": "✊", "paper": "✋", "scissors": "✌️"}

beats = {
    "rock": "scissors",   # rock crushes scissors
    "paper": "rock",      # paper covers rock
    "scissors": "paper"   # scissors cut paper
}

def show_menu():
    print("Lets play a game of Rock, Papper, Scissors!")
    print(f"1. {emojis['rock']} Rock")
    print(f"2. {emojis['paper']} Paper")
    print(f"3. {emojis['scissors']} Scissors")

def read_users_choice_number(): # This Reads the 1 2 3 input and converts to rock paper scissors
        while True:
            raw = input("Your choice (1/2/3): ").strip()
            if raw in ("1", "2", "3"):
                return options[int(raw) - 1]
            print("❌ Invalid. Type 1, 2, or 3.")
            
player_wins = 0
computer_wins = 0
WIN = 3  # first to 3 wins (best of 5)
round_no = 0 # keeps track of the times played, until 3 wins by one player
round_no += 1
print(f"\n— Round {round_no} —")

while player_wins < WIN and computer_wins < WIN:

    show_menu()
    user_choice = read_users_choice_number() # gets user choice
    computer_choice = random.choice(options) # gets computer choice

    print(f"ME: {emojis[user_choice]} {user_choice}")
    print(f"PC: {emojis[computer_choice]} {computer_choice}")

# This is to add a message for win  or lose or draw
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif beats[user_choice] == computer_choice:
        player_wins += 1
        print("YOUUUUUU WWWWWIIIIIINNNNN!!!!! 🎉")
    else:
      computer_wins += 1
      print("MACHINE WON, BEAT IT LOOSER!!!! YOU SUUUUCK!!!!😭")

    print(f"Score: You {player_wins} — {computer_wins} CPU") # prints score


if round_no == 2 and player_wins == 1 and computer_wins == 1:
    print("Round 3 is here, GO!")
elif round_no >= 3 and player_wins < WIN and computer_wins < WIN:
    print("Wa-ta-ga-ta-pi-tus-berry, okay?. Round continues!")
if player_wins == 2 and computer_wins == 2:
    print("⚔️ Round 5 is the decider!")
if player_wins == 2 and computer_wins < 2:
    print("🔥 Match point for YOU — next win takes it!")
elif computer_wins == 2 and player_wins < 2:
    print("⚠️ Match point for CPU — don’t drop the next one!")
elif round_no >= 5 and player_wins < WIN and computer_wins < WIN:
    print("🟡 Sudden death: first to 3 wins.")

print(f"Final Score: You {player_wins} — {computer_wins} CPU")