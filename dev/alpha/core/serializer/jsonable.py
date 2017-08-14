import json


class Jsonable(object):

    def __init__(self, *args):
        self.fields = args

    def __call__(self, cls):
        cls._jsonFields = self.fields

        def toDict(self):
            d = {}
            for f in self.__class__._jsonFields:
                v = self.__getattribute__ (f)
                if isinstance (v, list):
                    d [f] = [e.jsonDict if hasattr (e.__class__, '_jsonFields') else e for e in v]
                    continue
                d [f] = v.jsonDict if hasattr (v.__class__, '_jsonFields') else v
            return d
        cls.toDict = toDict

        oGetter = cls.__getattribute__

        def getter(self, key):
            if key == 'jsonDict': return self.toDict ()
            return oGetter (self, key)
        cls.__getattribute__ = getter

        return cls