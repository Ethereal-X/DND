from flask import render_template, request

def makechar(character):
    
    global elf_strength 
    elf_strength = 5
    global elf_dexterity 
    elf_dexterity = 9
    global elf_constitution 
    elf_constitution = 15
    
    global dwarf_strength
    dwarf_strength = 8
    global dwarf_dexterity 
    dwarf_dexterity = 2
    global dwarf_constitution 
    dwarf_constitution = 22
    
    global human_strength 
    human_strength = 6
    global human_dexterity 
    human_dexterity = 7
    global human_constitution
    human_constitution= 18
    
    if character == "elf":
        health = elf_constitution
        strength = elf_strength
        stats = "Your strength is " + str(elf_strength) + ", your dexterity is " + str(elf_dexterity) + ", and your constitution is " + str(elf_constitution)
        return stats, character, health, strength
    elif character == "dwarf":
        health = dwarf_constitution
        strength = dwarf_strength
        stats = "Your strength is " + str(dwarf_strength) + ", your dexterity is " + str(dwarf_dexterity) + ", and your constitution is " + str(dwarf_constitution)
        return stats, character, health, strength
    elif character == "human":
        health = human_constitution
        strength = human_strength
        stats = "Your strength is " + str(human_strength) + ", your dexterity is " + str(human_dexterity) + ", and your constitution is " + str(human_constitution)
        return stats, character, health, strength
    else:
        return("Please write human, elf, or dwarf with no caps or spaces")