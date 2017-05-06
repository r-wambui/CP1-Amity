import random

from persons import Fellow, Staff
from rooms import Office, LivingSpace


class Amity(object):

    def __init__(self):
        self.person = []
        self.staff = []
        self.fellow = []
        self.unallocated_person = []
        self.unaccomodated_fellow = []
        self.rooms = []
        self.offices = []
        self.livingspaces = []
        self.vacant_offices = []
        self.unvacant_offices = []
        self.vacant_livingspace = []
        self.unvacant_livingspace = []

    def allocate_office(self):
        if len(self.vacant_offices) > 0 and len(self.unallocated_person) > 0:
            secure_random = random.SystemRandom()
            person = secure_random.choice(self.unallocated_person)
            office = secure_random.choice(self.vacant_offices)

            if office.limit > len(office.occupants):
                office.occupants.append(person)
                self.unallocated_person.remove(person)
            else:
                self.unvacant_offices.append(office)
                self.vacant_offices.remove(office)
                print ('An office can only have a maximum of 6 people')

    def allocate_livingspace(self):
        if len(self.vacant_livingspace) > 0 and len(self.unaccomodated_fellow) > 0:
            secure_random = random.SystemRandom()
            person = secure_random.choice(self.unaccomodated_fellow)
            livingspace = secure_random.choice(self.vacant_livingspace)

            if livingspace.limit > len(livingspace.occupants):
                livingspace.occupants.append(person)
                self.unaccomodated_fellow.remove(person)
            else:
                self.unvacant_livingspace.append(livingspace)
                self.vacant_livingspace.remove(livingspace)
                print ('A livingspace can only accomodate 4 fellows')

    def add_person(self, first_name, last_name, job_type, want_accomodation):
        if type(first_name) == str and type(last_name) == str and type(job_type) == str:
            if job_type.title() == 'Staff' or job_type.title() == 'Fellow':
                if [person for person in self.person if first_name == person.first_name and last_name == person.last_name]:
                    print('The person exists')
                    return 'Person already Exists'
                if job_type.title() == 'Staff':
                    person = Staff(first_name, last_name,
                                   job_type, want_accomodation)
                    self.person.append(person)
                    self.staff.append(person)
                    self.unallocated_person.append(person)
                    self.allocate_office()
                    print ('Person added successfully')

                    if want_accomodation == 'Y':
                        return 'A staff cannot be allocated a living space'

                elif job_type.title() == 'Fellow':
                    person = Fellow(first_name, last_name,
                                    job_type, want_accomodation)
                    self.person.append(person)
                    self.fellow.append(person)
                    self.unallocated_person.append(person)
                    self.unaccomodated_fellow.append(person)
                    self.allocate_office()
                    return 'Person added successfully'

                    if want_accomodation == 'Y':
                        self.allocate_livingspace()
                    else:
                        pass

            else:
                return 'The person role can only be a staff or a fellow'

        else:
            return ('Invalid input')

    def create_room(self, room_name, room_type):
        if type(room_name) == str and type(room_type) == str:
            if [room for room in self.rooms if room_name == room.room_name]:
                print("{} Already created.".format(room_name))
                return 'Room already created'
            if room_type == 'Office':
                room = Office(room_name, room_type)
                self.rooms.append(room)
                self.offices.append(room)
                self.vacant_offices.append(room)
                return ('Room created successfully')

            elif room_type == 'LivingSpace':
                room = LivingSpace(room_name, room_type)
                self.rooms.append(room)
                self.livingspaces.append(room)
                self.vacant_livingspace.append(room)
                return ('Room created successfully')
        else:
            return ('Invalid Input')

    def reallocate_person(self, first_name, room_name):
        # Checking if the new room exist
        for new_room in self.vacant_offices:
            if new_room.room_name == room_name:
                # Checking if person was previously allocated
                for room in self.rooms:
                    for person in self.person:
                        if person.first_name in [person.first_name for person in room.occupants]:
                            if new_room == room:
                                print (
                                    'You cannot be re-allocated to the same room')
                        else:
                            room.occupants.remove(person)
                            # Allocate to the new room
                            new_room.occupants.append(person)
                            print ('successfully reallocated')

            else:
                return 'Room does not exist or unvacant'

        # for room in self.livingspaces:

        # if[person for person in room.occupants if person.first_name == first_name]:
        # for vacant in self.vacant_livingspace:
        # if vacant.room_name == new_room:
        # vacant.occupants.append(person)
        # room.occupants.remove(person)
        # return 'You have been re-allocated to new Livingspac'

    def load_people(self):
        pass

    def print_allocations(self):
        pass

    def print_unallocated(self):
        pass

    def print_rooms(self):
        pass

    def save_state(self, db_name):
        pass

    def load_state(self, db_name):
        pass
