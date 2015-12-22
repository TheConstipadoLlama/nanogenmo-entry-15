from random import randint

def guild_party(n):
    names = ["King Arthur", "Flagg", "Squirtle", "Mob"]
    fool = [" the fool of Altera. ", " the infamously awesome scrub that personally wet himself. ", " picks their nose. ", " kills the fiercest cucco of hyrule. "]
    count = 0
    f = open('myfile.txt', 'a')
    while count < n:
        name_random_number = randint(0, 3)
        fool_random_number = randint(0, 3)
        
        f.write(names [name_random_number] + fool [fool_random_number])
        count += 1
    f.write("\n")

count = 0
while count < 1000:
    guild_party(20)
    count += 1
