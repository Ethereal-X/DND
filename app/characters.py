import DND.html
import DND.css


elf_strength = 5;
elf_dexterity = 9;
elf_constitution = 15;

dwarf_strength = 8;
dwarf_dexterity = 2;
dwarf_constition = 22;

human_strength = 6;
human_dexterity = 7;
human_constitution = 18;

choice = str(.html);

if choice == "elf":
    strength = elf_strength;
    dexterity = elf_dexterity;
    constitution = elf_constitution
#print("Your strength is " + strength + ", your dexterity is " + dexterity + ", and your constitution is " + constitution)
elif input == "dwarf":
    strength = dwarf_strength;
    dexterity = dwarf_dexterity;
    constitution = dwarf_constition;
    print("Your strength is " + strength + ", your dexterity is " + dexterity + ", and your constitution is " + constitution)

elif input == "human":
    strength = 6;
    dexterity = 7;
    constitution = 18;
    print("Your strength is " + strength + ", your dexterity is " + dexterity + ", and your constitution is " + constitution)
    
else:
    print("Please write human, elf, or dwarf with no caps or spaces")