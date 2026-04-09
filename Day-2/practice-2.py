import random
from collections import Counter
def simulate_rolling_die(n):
    rolling  = [random.randint(1,6) for i in range(n)]
    return rolling

rollings = simulate_rolling_die(10)
print(Counter(rollings).most_common(6))

