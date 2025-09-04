messages = [
    "Click 1: nothing good is born from lies",
    "Click 2: I can do this all day.",
    "Click 3: With Great Power...",
    "Click 4: comes great responsibility.",
    "Click 5: I am Inevitable.",
    "Click 6: And i am ironman.",
    "Click 7: I love you 3000.",
]

clicks = 0 # we start at 0 clicks to count up from

while clicks < 7: # while we have less than 7 clicks this is the condition
    input("Press enter to click") # wait for the user to press enter
    clicks += 1 # add one to clicks

    print(f"clicks: {clicks}/7") # print the number of clicks
    print(messages[clicks - 1])  # print the message for the current click

# After the 7th click, OUTSIDE the loop:
print("WAKANDA FOR THE MOMENT!")