import random

from persons import Fellow, Staff
from rooms import Office, LivingSpace


class Amity(object):

    def __init__(self):
        self.persons = []
        self.staffs = []
        self.fellows = []
        self.unallocated_persons = []
        self.unaccomodated_fellows = []
        self.rooms = []
        self.offices = []
        self.livingspaces = []
        self.vacant_offices = []
        self.unvacant_offices = []
        self.vacant_livingspaces = []
        self.unvacant_livingspaces = []

    def allocate_office(self):
        if len(self.vacant_offices) > 0 and len(self.unallocated_persons) > 0:
            secure_random = random.SystemRandom()
            person = secure_random.choice(self.unallocated_persons)
            office = secure_random.choice(self.vacant_offices)

            if office.limit > len(office.occupants):
                office.occupants.append(person)
                self.unallocated_persons.remove(person)
            else:
                self.unvacant_offices.append(office)
                self.vacant_offices.remove(office)
                print ('An office can only have a maximum of 6 people')

    def allocate_livingspace(self):
        if len(self.vacant_livingspaces) > 0 and len(self.unaccomodated_fellows) > 0:
            secure_random = random.SystemRandom()
            person = secure_random.choice(self.unaccomodated_fellows)
            livingspace = secure_random.choice(self.vacant_livingspaces)

            if livingspace.limit > len(livingspace.occupants):
                livingspace.occupants.append(person)
                self.unaccomodated_fellows.remove(person)
            else:
                self.unvacant_livingspaces.append(livingspace)
                self.vacant_livingspaces.remove(livingspace)
                print ('A livingspace can only accomodate 4 fellows')

    def add_person(self, first_name, last_name, job_type, want_accomodation):
        if type(first_name) == str and type(last_name) == str and type(job_type) == str:
            if job_type.title() == 'Staff' or job_type.title() == 'Fellow':
                if [person for person in self.persons if first_name == person.first_name and last_name == person.last_name]:
                    print('The person exists')
                    return 'Person already Exists'
                if job_type.title() == 'Staff':
                    person = Staff(first_name, last_name,
                                   job_type, want_accomodation)
                    self.persons.append(person)
                    self.staffs.append(person)
                    self.unallocated_persons.append(person)
                    self.allocate_office()
                    print ('Person added successfully')

                    if want_accomodation == 'Y':
                        print ('A staff cannot be allocated a living space')
                        return 'A staff cannot be allocated a living space'

                elif job_type.title() == 'Fellow':
                    person = Fellow(first_name, last_name,
                                    job_type, want_accomodation)
                    self.persons.append(person)
                    self.fellows.append(person)
                    self.unallocated_persons.append(person)
                    self.unaccomodated_fellows.append(person)
                    self.allocate_office()
                    print('Person added successfully')
                    return 'Person added successfully'

                    if want_accomodation == 'Y':
                        self.allocate_livingspace()
                    else:
                        pass

            else:
                print('The person role can only be a staff or a fellow')
                return 'The person role can only be a staff or a fellow'

        else:
            print ('Invalid input')
            return 'Invalid input'

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
                print('Room created successfully')
                return 'Room created successfully'

            elif room_type == 'LivingSpace':
                room = LivingSpace(room_name, room_type)

                self.rooms.append(room)
                self.livingspaces.append(room)
                self.vacant_livingspaces.append(room)
                print('Room created successfully')
                return 'Room created successfully'
        else:
            print('Invalid Input')
            return 'Invalid Input'

    def get_room(self, first_name):
        for room in self.rooms:
            for person in room.occupants:
                if person.first_name in room.occupants:
                    return room

    def reallocate_person(self, first_name, room_name):
        # check type of room_name - office or living space
        for room in self.rooms:
            if room.room_type == 'Office':
            # checking if the a new_office has vacancy
                if not [new_room for new_room in self.vacant_offices if room_name == new_room.room_name]:
                    print ('{}is not vacant'.format(room_name))
                    return '{}is not vacant'.format(room_name)
             # check if the person is an occupant of room_name
                if [person for person in new_room.occupants if first_name == person.first_name]:
                    print('you cannot be reallocated to the same room')
                    return 'you cannot be reallocated to the same room'
                else:
                    self.get_room(first_name).remove(first_name)
                    new_room.occupants.append(person)

                # assumption - room_name.occupants gives you all the current occupants
                # if person is an occupant - show error and exit
                # else add person to room and remove from previous room
                # create a function that returns either room identifier (for either office or living space) or None
                # eg get_room('user_id', '[O|L]')
            elif room.room_type == 'Livingspace':
                if not [new_room for new_room in self.vacant_livingspaces if room_name == new_room.room_name]:
                    print('{}is not vacant'.format(room_name))
                    return '{}is not vacant'.format(room_name)

                if [person for person in new_room.occupants if first_name == person.first_name]:
                    print('you cannot be reallocated to the same room')
                    return 'you cannot be reallocated to the same room'
                else:
                    self.get_room(
                        first_name).room.occupants.\
                        remove(first_name)
                    new_room.occupants.append(person)
    # def reaccomodate_person(self, first_name, room_name):
    #     # checking if new_livingspace is vacant or exist
    #     if not [new_room for new_room in self.vacant_livingspaces if room_name == new_room.room_name]:
    #         return '{} is not vacant'.format(room_name)
    #     # checking if the person was previously accomodated
    #     for room in self.livingspaces:
    #         if [person for person in room.occupants if first_name == person.first_name]:
    #             room.occupants.remove(person)
    #             # re-accomodate to the new livingspace
    #             new_room.occupants.append(person)
    #             return 'Successfully reaccomodated'

    def load_people(self, file_name):

        with open(file_name, 'r') as f:
            people = f.readlines()
            for person in people:
                person = person.split()
                if person:
                    first_name = person[0]
                    last_name = person[1]
                    job_type = person[2]
                    if len(person) == 4:
                        want_accomodation = person[3]
                    else:
                        want_accomodation = None
                    self.add_person(first_name, last_name, job_type, want_accomodation)
                    print ('Adding people from the txt file successful')

    def print_allocations(self, file_name):
        output = ''
        #check the room name and type from the room list
        for room in self.rooms:
            output += room.room_name + room.room_type +'\n'
            output += '-' * 40 + '\n'
            if room.occupants:
               output += ','.join(person.first_name + person.last_name for person in room.occupants) + '\n'
            else:
                output += 'This room is empty.\n'
        # if not [room for room  in self.rooms]:
        #     output += 'The room does not exist.\n'
        print output
        #save the allocations of a text file
        if file_name:
            with open(file_name, 'w') as f:
                f.write(output)
                print 'Allocations have been saved to the file: \n'
                print file_name

    def print_unallocated(self, file_name):
        self.unallocated = self.unaccomodated_fellows + self.unallocated_persons
        output = ''
        for person in self.persons:
                if person in self.unallocated:
                    output += (person.first_name + person.last_name) + '\n'
        print output
        if file_name:
            with open(file_name, 'w') as f:
                f.write(output)
                print 'Unallocated people have been saved to the file: \n'
                print file_name

    def print_room(self, room_name):
        if room_name not in [room.room_name for room in self.rooms]:
            print ('The room is not available')
        for room in self.rooms:
            if room.room_name == room_name:
                print (room.room_name + room.room_type)
                if room.occupants:
                    for person in room.occupants:
                        print (person.first_name + person.last_name + person.job_type)
                else:
                    print 'this room has no occupants'
      

    def save_state(self, db_name):
        pass

    def load_state(self, db_name):
        pass
