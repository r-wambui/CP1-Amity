from persons import Person, Fellow, Staff
from rooms import Room, Office, LivingSpace


class Amity(object):

    def __init__(self):
        pass

    def add_person(self, fname, lname, role, want_accomondation):
        pass

    def create_room(self, room_name, status):
        pass

    def allocate_person(self, fname, lname, role, room_name):

        pass

    def reallocate_person(self, fname, lname, role, room_name):
        pass

    def load_people(self):
        pass

    def print_allocations(self):
        pass

    def print_unallocates(self):
        pass

    def print_rooms(self):
        pass
