# declare three character#

wizard = "Wizard"
elf = "Elf"
human = "Human"

# HIT POINT FOR CHARACTER#
wizard_hp = 70
elf_hp = 100
human_hp = 150

# damage for character
wizard_damage = 150
elf_damage = 100
human_damage = 20

# hp and damage for dragon#
dragon_hp = 300
dragon_damage = 50


print("1) Human")
print("2) Elf ")
print("3) wizard")

character = input("please select your character: ")

while True:
    if character == "1":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("character ={} my_hp={} damage={}".
              format(character, my_hp, my_damage))
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("character ={} my_hp={} damage={}".
              format(character, my_hp, my_damage))
        break
    if character == "3":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("character ={} my_hp={} damage={}".
              format(character, my_hp, my_damage))
        break
    else:
        print("invalid response")
        break
while True:
    dragon_hp = dragon_hp-my_damage
    print("the", character, "damage the dragon")
    if dragon_hp <= 0:
        print("the dragon lost the battle")
        break
    my_hp = my_hp-dragon_damage
    print(character, my_hp, "your character has been damage by the dragon")
    if my_hp <= 0:
        print("your", character, "lost the battle")
        break
