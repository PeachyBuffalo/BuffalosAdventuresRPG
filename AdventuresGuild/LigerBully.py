def start():
  print("\nYou find yourself panting from a Liger that chased you across open plains. \n BTWs you are a Buffalo.")
  print("There is a cave you can hid in to your left and river to cross on your right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    cave_entrance()
  elif "r" in answer:
    river_entrance()
  else:
    game_over("Your poor decision making led the Liger right to you!")

# cave_entrance
def cave_entrance():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nYou slide left into the cave.")
  print("Luckily you hear the Liger run past and sniff the riverside.")
  print("Without thinking you find yourself backed up against the wall of the cave.")
  print("What would you do? (1 or 2)")
  print("1). Rest your eyes for a few minutes.")
  print("2). Check the entrance of the cave.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("You wake up to roar of the Liger as it sprints towards you. \nIn the fog of your confusion you are frozen unable to move as the Liger lunges towards you.")
  elif answer == "2":
    # Liger heads to the river
    print("\nLuckily the Liger has moved on, you should continue on before it \ncomes back...")
    open_plains_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Your poor choices led the Liger right to you! \nIn the fog of your confusion you are frozen unable to move as the Liger lunges towards you.")

# river_entrance
def river_entrance():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nYou step into a roaring river.")
  print("You feel the water pulling at your hindlegs.\nWhat would you do? (1 or 2)")
  print("1). Turn back and head for the cave.")
  print("2). Try to cross the river.")

  # take input()
  answer = input(">")

  if answer == "1":
    # head into cave_entrance()
    cave_entrance()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The current pulls you underwater with no  sight of the surface. \nEverything fades to black.")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")
# start the game
start()