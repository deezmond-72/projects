print("Coin Flip Simulation")

import random
import time

def Cointoss(num_tosses):
    heads = 0

    for _ in range(num_tosses):
        if random.random() < 0.5:
            heads += 1

    return heads / num_tosses


def run_simulations(num_experiments, tosses_per_experiment):
    total = 0
    for _ in range (num_experiments):
        total += Cointoss(tosses_per_experiment)
    return total / num_experiments

start = time.time()

average = run_simulations(
    num_experiments=10_000
    , tosses_per_experiment=1000
)
end = time.time()

print(f"\n Average Heads: {average:.4f} \n")
print (f"\n Time Taken: {end-start:.3f} seconds \n")


proportion = Cointoss(1000)
print(f"\n Proportion of heads after 1000 flips: {proportion:.2f} \n")