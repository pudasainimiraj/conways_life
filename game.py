import Rules from setup.py

class Game():

    def getName()-> str:
        return "Conways Game of Life"

    def rulesApplied(bool isAlive, int neighbourCount) -> int:
        if(isAlive):
            return (neighbourCount==2||neighbourCount==3)
        else:
            return (neighbourCount==3)
        return isAlive
