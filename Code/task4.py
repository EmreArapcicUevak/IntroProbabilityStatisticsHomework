import random

def get_average_roll(num_of_rolls):
    total_sum = 0
    for _ in range(num_of_rolls):
        total_sum += random.randint(1, 12)
    return total_sum / num_of_rolls

# Run the simulation for different numbers of rolls and print the averages
print(f"Average for 100 rolls: {get_average_roll(100):.2f}")
print(f"Average for 1,000 rolls: {get_average_roll(1000):.2f}")
print(f"Average for 10,000 rolls: {get_average_roll(10000):.2f}")
print(f"Average for 100,000 rolls: {get_average_roll(100000):.2f}")
