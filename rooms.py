class Room(object):

    def __init__(self, name, status):
        self.name = name
        self.status = status


class Office(Room):

    def __init__(self, name, limit=4):
        self.name = name
        self.limit = limit


class LivingSpace(Room):

    def __init__(self, name, limit=6):
        self.name = name
        self.limit
