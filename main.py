# Whole code is meant to log a bout and provide which touch occured most often

import sys
import json
from collections import Counter

# Figure out bout type which will determine parameters for later inputs
# if a valid bout type is entered the program will continue by asking for score

bout_type = input("DE or Pool: ")
bout_type = bout_type.strip().lower()

if bout_type == "de" or bout_type == "pool":
 score = input("What was the score: ")
else:
    print("Not a valid bout type.")
    sys.exit(1)

# This section checks if the score entered is valid

if score == '':
   print("No Score Entered")
   sys.exit(2)
if "-" not in score:
   print("Invalid Score")
   sys.exit()

score = score.split("-")

if len(score) != 2:
   print("Invalid Score")
   sys.exit()

for s in score:
   if not s.isdigit():
      print("Invalid Score")
      sys.exit()

total_touches = int(score[0])+ int(score[1])
p1 = int(score[0])
p2 = int(score[1])

max_score = 15 if bout_type == 'de' else 5

if p1 == p2:
   print ("Invalid Score(no ties)")
   sys.exit()

if p1 > max_score or p2 > max_score:
   print("Score Exceeds Maximum")
   sys.exit()

if max(p1,p2) != max_score:
   print ("Invalid Score (no winner)")
   sys.exit()

# This section asks user to input the actions that happened in the bout

valid_touches = ["attack","parry","remise","counter"]

touches = input("What were the touches that were scored:")

touches = touches.split(",")
touches = [t.strip().lower() for t in touches]

# This part verfies if the touches entered are valid

if not touches or touches == ['']:
   print("Error: no touches entered")
   sys.exit(5)

for touch in touches:
   if touch not in valid_touches:
      print("Invalid Touch Entered")
      sys.exit(6)

if len(touches) != total_touches:
   print("Error: Number of touches does not match score!")
   sys.exit(7)

# This section takes the touches entered above and asks for the user to
# determine who scored on each touch it also checks if the input is valid

counter = 0
new_touches = []
me_counter = 0
opp_counter = 0

for touch in touches:
   counter += 1
   scorer = input(f'Who scored touch #{counter} ({touch}): ')
   scorer = scorer.lower().strip()

   if scorer not in ['me','opp']:
      print("Invalid Scorer")
      sys.exit()
   elif scorer == 'me':
      me_counter += 1
   elif scorer == 'opp':
      opp_counter += 1
   new_touches.append(touch + "_" + scorer)

if opp_counter != max_score and me_counter != max_score:
   print("A fencer must have scored enough touches to win")
   sys.exit()

touches = new_touches

# This section calculates key statistics from the bout

touch_freq = Counter(touches)
print(touch_freq)

most_common = touch_freq.most_common(1)
print("Most Common Touch:", most_common[0][0])

actions = [touch.split('_')[0] for touch in touches if touch.endswith('_me')]
my_touch_freq = Counter(actions)
my_touch_freq = my_touch_freq.most_common(1)

if my_touch_freq:
   print("Your most successful action was:", my_touch_freq[0][0])


# This part is designed to officially log and store bout data
# entered above

bout_data = {
    "bout_type": bout_type,
    "score": [p1, p2],
    "touches": touches
}

try:
    with open("bouts.json", "r") as file:
        bouts = json.load(file)
except:
    bouts = []

bouts.append(bout_data)

with open("bouts.json", "w") as file:
    json.dump(bouts, file, indent=4)