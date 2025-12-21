print("Started")

import random
import time

def LuckTome(Attempts):
    Luck_Tome_Drops = 0

    for _ in range(Attempts):
        if random.random() < 0.0001:
            Luck_Tome_Drops += 1

    
    print(f"\nOut of {Attempts} enemies killed, you have {Luck_Tome_Drops} Luck Tome Drops!")
    average_chance = Luck_Tome_Drops / Attempts * 100
    print(f"\nAverage Chance in {Attempts} enemies killed: {average_chance:.4f}%")

    return Luck_Tome_Drops

LuckTome(100000)
