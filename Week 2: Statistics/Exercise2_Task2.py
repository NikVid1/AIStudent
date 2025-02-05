import numpy as np

dice_rolls = np.random.randint(1, 7, size=1000)

primes = [2, 3, 5]

prime_rolls = 0
for i in range(len(dice_rolls)):
    if dice_rolls[i] in primes:
        prime_rolls += 1

p_prime = prime_rolls / len(dice_rolls)
print("The probability of rolling a prime number is roughly", p_prime*100, "%")

odd = [1, 3, 5]

odd_primes = 0
odds = 0
for i in range(len(dice_rolls)):
    if dice_rolls[i] in odd and dice_rolls[i] in primes:
        odd_primes += 1
    if dice_rolls[i] in odd:
        odds += 1

p_prime_and_odd = odd_primes / odds

print("The probability of rolling a prime number and an odd number is roughly", p_prime_and_odd*100, "%")

