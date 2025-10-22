import random

class Player:
    xpHad = 0
    playerLevel = 1
    def __init__(self):
        return
    def levelUpCheck(self, xpGained):
        if xpNeeded(self.playerLevel) <= xpGained + self.xpHad:
            self.playerLevel+=1
            return True
        return False
 
def xpNeeded(level):
    return (level * someVariable) # set someVariable equal to something and/or write and equation
    
def enemyLevel(playerLevel):
    enemyLevel = playerLevel + random.randint(-5, 5)
    if enemyLevel < 1:
        enemyLevel = 1
    return enemyLevel

player = Player()








