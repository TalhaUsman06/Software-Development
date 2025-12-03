import random #Library to generate random number 

# Start Do-While menu loop
while True:
    print("\n--- GUESS THE NUMBER GAME ---")
    print("1. Play Game")
    print("2. Exit")
    print("\n-----------------------------")
    
    menu_choice = input("Enter your choice (1 or 2): ")

    if menu_choice == '1':
        # --- GAME START ---
        secret_number = random.randint(1, 100)
        #randit selects random number between the given range in this case 1 to 100.
        max_attempts = 7
        attempts_taken = 0
        has_won = False
        
        print(f"\nI have chosen a number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess it.")

        # Loop for the game logic
        while attempts_taken < max_attempts:
            #f before "" in print statement is to look for curly braces which are variables
            user_input = input(f"\nAttempt {attempts_taken + 1}/{max_attempts}: Enter your guess: ")

            # Validate that the input is a number
            if not user_input.isdigit():
                print(">> Invalid entry! Please enter a whole number between 1 and 100.")
                continue # Skip the rest of the loop and ask again
            
            guess = int(user_input)
            attempts_taken += 1
            
             # Validate that the input within Range
            if guess > 100 or guess < 1:
                print(">> Invalid entry! Please enter a number between 1 and 100.")
                continue # Skip the rest of the loop and ask again

            # Check the guess
            if guess < secret_number:
                print("Too low! Try a bigger number.")
            elif guess > secret_number:
                print("Too high! Try a smaller number.")
            else:
                print(f"*** CONGRATULATIONS! You guessed the {secret_number} correctly! ***")
                has_won = True
                
                if attempts_taken<5:
                    print("You are a genius you guessed faster than 85% of players.")
                else:
                    break # Exit the guessing loop
        
        # Check if the user lost after running out of attempts
        if not has_won:
            #f before "" in print statement is to look for curly braces which are variables
            print(f"\nGame Over! You ran out of 7 attempts.")
            print(f"The number was: {secret_number}")
            
    elif menu_choice == '2':
        # --- EXIT ---
        print("\nThank you for playing. Goodbye!")
        break # Breaks the  while True loop, ending the program
        
    else:
        # --- INVALID MENU OPTION ---
        print("\n>> Invalid option selected. Please try again.")