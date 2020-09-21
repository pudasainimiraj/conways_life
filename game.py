from setup import setRules

@setRules.register
class Game(setRules):

    def getName():
        return "Conways Game of Life"

    def rulesApplied(isAlive, neighbourCount):
        if(isAlive):
            return (neighbourCount==2 | neighbourCount==3)
        else:
            return (neighbourCount==3)
        return isAlive

#print(issubclass(Game,setRules))
#s print(Game.__mro__)
