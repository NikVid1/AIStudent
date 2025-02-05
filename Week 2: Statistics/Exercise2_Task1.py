import numpy as np

coin_tosses = np.random.choice(['H', 'T'], size=1000)

num_heads = 0
for i in range(len(coin_tosses)):
    if coin_tosses[i] == 'H':
        num_heads += 1

#print(num_heads)

heads_ratio = num_heads/len(coin_tosses)
print(f"there is a {heads_ratio*100}% chance of getting heads")
