
import random
def Fight (health,strength,character, stats):
    goblin_constitution = 20;
    goblin_strength = 6;
    while (goblin_constitution > 0):
        goblin_constitution = goblin_constitution - random.randint(1,strength) 
        print(goblin_constitution)
        health = health - random.randint(1,goblin_strength)
        print(health)
    
    if goblin_constitution > health:
        return "You've lost"
    else:
        return "You won"
    
    

    
