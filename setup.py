
# program conways game of life

#enforcing the subclass virtulization of abstract class using the abc module
import abc

# -*- coding: utf-8 -*-
# aurthur : Miraj Pudasaini
#Interface(Metaclass) setRules implements ABCMeta


class setRules(metaclass=abc.ABCMeta):
    """A meta class implementations for rules setup"""
    # def __instancecheck__(cls,instance):
    #     return cls.__subclasscheck__(type(instance))

    @classmethod
    def __subclasshook__(cls,subclass):
        return(hasattr(subclass,"getName") and
                callable(subclass.getName) and
                hasattr(subclass,'rulesApplied') and
                callable(subclass.rulesApplied) or NotImplemented)

setRules.register(str)
