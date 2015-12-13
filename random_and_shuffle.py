import random

values = [1, 2, 3, 4, 5, 6]

# pick random item out of a sequence
random.choice(values)

# take a sampling of n items
random.sample(values, 3)

# shuffle items
random.shuffle(values)

# produce random integer
random.randint(0, 10)

# produce uniform float values in the range 0 to 1
random.random()  # 0.9406677561675867

# get n random bits expressed as integer
random.getrandbits(200)
# 335837000776573622800628485064121869519521710558559406913275
