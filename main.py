import random

def simulate_monty_hall(num_trials):
    switch_wins = 0
    stay_wins = 0

    for i in range(num_trials):
        # Randomly place the car behind one of the three doors
        car_position = random.randint(0, 2)

        # Contestant makes a random initial choice
        contestant_choice = random.randint(0, 2)

        # Host opens one of the remaining doors that doesn't have the car
        remaining_doors = [0, 1, 2]
        remaining_doors.remove(contestant_choice)
        if car_position in remaining_doors:
            remaining_doors.remove(car_position)
        host_opens = random.choice(remaining_doors)

        # Determine the remaining closed door
        remaining_doors = [0, 1, 2]
        remaining_doors.remove(contestant_choice)
        remaining_doors.remove(host_opens)
        remaining_closed_door = remaining_doors[0]

        # Check if switching wins
        if remaining_closed_door == car_position:
            switch_wins += 1

        # Check if staying wins
        if contestant_choice == car_position:
            stay_wins += 1

    return switch_wins, stay_wins

# Ask the user for number of trials
number_of_trials = input("Enter the number of trials for Monty Hall simulation: ")

# Run the simulation
switch_wins, stay_wins = simulate_monty_hall(int(number_of_trials))

# print results
print(f"Switch wins: {switch_wins} out of {number_of_trials}")
print(f"Stay wins: {stay_wins} out of {number_of_trials}")
