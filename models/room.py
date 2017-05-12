class Room(object):

    def __init__(self, room_name, room_type, limit):
        self.room_name = room_name
        self.room_type = room_type
        self.limit = limit


class Office(Room):

    def __init__(self, room_name, room_type, limit=6):
        self.occupants = []
        super(Office, self).__init__(room_name, room_type, limit)


class LivingSpace(Room):

    def __init__(self, room_name, room_type, limit=4):
        self.occupants = []
        super(LivingSpace, self).__init__(room_name, room_type, limit)
