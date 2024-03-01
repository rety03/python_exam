import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 != 0: # defining odd numbers
        random_numbers[i] = None  # Marking odd numbers for removal
    else:
        random_numbers[i] *= 2  # Double even numbers
random_numbers = [num for num in random_numbers if num is not None] #removing odd numbers

print(random_numbers)