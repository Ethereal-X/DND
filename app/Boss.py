goblin_constitution = 12;
goblin_strength = 5;
import random
def Fight (health,strength,stats,character):
    while (goblin_constitution > 0):
        goblin_constitution - random.randint(1,strength)
        print(goblin_constitution)
        health - random.randint(1,goblin_strength)
        print(health)
    
    if goblin_constitution > health:
        return "You've lost"
    else:
        return "You won"
    
    

    
