from random import randint
    
def guild_party(n):
    names = ["King Arthur", "Flagg", "Squirtle", "Mob"]
    fool = [" the fool of Altera. ", " the infamously awesome scrub that personally wet himself. ", " picks their nose. ", " kills the fiercest cucco of hyrule. "]
    f = open('myfile.txt', 'a')
    count = 0
    while count < n:
        name_random_number = randint(0, 3)
        fool_random_number = randint(0, 3)
        f.write(names [name_random_number] + fool [fool_random_number])
        count += 1
    f.write("\n")

g = open('myfile.txt', 'w')
g.write('the eyes of the holy grail nest 100. ')
g.write("\n")
g.close()

count = 0
while count < 1000:
    guild_party(20)
    count += 1

print count
