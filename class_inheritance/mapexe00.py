#!/usr/bin/python3

class Mapping:

    pre_items = []
    new_items = []

    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable) #calls a private copy of update() so items_list will not be empty ever

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method



class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)




itms1 = ['rice', 'beans']
itms2 = ['salads', 'beaf']

itm = Mapping(itms1)
print(itm.items_list)

itm.update(itms2)
print(itm.items_list)

