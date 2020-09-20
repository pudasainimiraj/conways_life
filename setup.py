# program conways game of life

# interfaces (virtual classes implementations)

class setRules(type):
    """A meta class implementations for rules setup"""
    def __instancecheck__(cls,instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls,instance):
        return(hasattr(subclass,"getName") and
                callable(subclass.getName) and
                hasattr(subclass."rulesApplied") and
                callable(subclass.rulesApplied))

class Rules(metaclass=setRules):
    pass
