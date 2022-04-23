import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items(): #loop
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list) #Random picker

other_weights = {
    'green': 1,
    'yellow': 2,
    'red': 3
}

print(weighted_lottery(other_weights))