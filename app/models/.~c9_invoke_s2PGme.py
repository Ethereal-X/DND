
def makechar(choice):
    
    global elf_strength 
    elf_strength = 5;
    global elf_dexterity 
    elf_dexterity = 9;
    global elf_constitution 
    elf_constitution = 15;
    
    global dwarf_strength
    dwarf_strength = 8;
    global dwarf_dexterity 
    dwarf_dexterity = 2;
    global dwarf_constitution 
    dwarf_constitution = 22;
    
    global human_strength 
    human_strength = 6;
    global human_dexterity = 7;
    global human_constitution
    human_constitution= 18;
    
    if choice == "elf":
        global elf_strength;
        global elf_dexterity;
        global elf_constitution;
        return("Your strength is " + str(elf_strength) + ", your dexterity is " + str(elf_dexterity) + ", and your constitution is " + str(elf_constitution))
    elif input == "dwarf":
        global dwarf_strength
        global dwarf_dexterity
        global dwarf_constitution
        print("Your strength is " + str(dwarf_strength) + ", your dexterity is " + str(dwarf_dexterity) + ", and your constitution is " + str(dwarf_constitution))
    
    elif input == "human":
        global human_strength 
        global human_dexterity
        global human_constitution
        print("Your strength is " + str(human_strength) + ", your dexterity is " + str(human_dexterity) + ", and your constitution is " + str(human_constitution))
        
    else:
        print("Please write human, elf, or dwarf with no caps or spaces")