import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Column, Table
from sqlalchemy.ext.declarative import declarative_base

from persons import Fellow, Staff
from rooms import Office, LivingSpace
from db.database import Person, Room, Base


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
        """Method that allocate people to offices at random """
        if len(self.vacant_offices) > 0 and len(self.unallocated_persons) > 0:
            secure_random = random.SystemRandom()
            person = self.unallocated_persons[-1]
            office = secure_random.choice(self.vacant_offices)

            if office.limit > len(office.occupants):
                office.occupants.append(person)
                self.unallocated_persons.remove(person)
            else:
                self.unvacant_offices.append(office)
                self.vacant_offices.remove(office)
                print ('An office can only have a maximum of 6 people')
                return 'An office can only have a maximum of 6 people'

    def allocate_livingspace(self):
        """ Method which allocate people to livingspaces at random"""
        if len(self.vacant_livingspaces) > 0 and len(self.unaccomodated_fellows) > 0:
            secure_random = random.SystemRandom()
            person = self.unaccomodated_fellows[-1]
            livingspace = secure_random.choice(self.vacant_livingspaces)

            if livingspace.limit > len(livingspace.occupants):
                livingspace.occupants.append(person)
                self.unaccomodated_fellows.remove(person)
            else:
                self.unvacant_livingspaces.append(livingspace)
                self.vacant_livingspaces.remove(livingspace)
                print ('A livingspace can only accomodate 4 fellows')

    def add_person(self, first_name, last_name, job_type, want_accomodation=None):
        """ Adding people to amity system"""
        if type(first_name) == str and type(last_name) == str and type(job_type) == str:

            if [person for person in self.persons
                if first_name.upper() == person.first_name.upper() and
                    last_name.upper() == person.last_name.upper()]:
                print('The person exists')
                return 'Person already Exists'

            if job_type == 'STAFF' or job_type == 'staff':
                person = Staff(first_name.upper(), last_name.upper(),
                               job_type.upper(), want_accomodation)
                self.persons.append(person)
                self.staffs.append(person)
                self.unallocated_persons.append(person)
                self.allocate_office()
                print ('Person added successfully')

                if want_accomodation == 'Y':
                    return 'A staff cannot be allocated a living space'

            elif job_type == 'FELLOW' or job_type == 'fellow':
                person = Fellow(first_name.upper(), last_name.upper(),
                                job_type.upper(), want_accomodation)
                self.persons.append(person)
                self.fellows.append(person)
                self.unallocated_persons.append(person)
                self.unaccomodated_fellows.append(person)
                self.allocate_office()

                if want_accomodation == 'Y':
                    self.allocate_livingspace()
                    return 'Person added successfully'

            else:
                return 'The person role can only be a staff or a fellow'

        else:
            print ('Invalid input')
            return 'Invalid input'

    def create_room(self, room_name, room_type):
        """ Method that creates rooms, both offices and livingspaces"""
        if type(room_name) == str and type(room_type) == str:

            if [room for room in self.rooms
                if room_name.upper() == room.room_name.upper() and
                    room_type.upper() == room.room_type.upper()]:
                print('room already exist')
                return 'Room already created'
            if room_type == 'office' or room_type == 'OFFICE':
                room = Office(room_name.upper(), room_type.upper())
                self.rooms.append(room)
                self.offices.append(room)
                self.vacant_offices.append(room)
                return 'Room created successfully'

            elif room_type == 'livingspace' or room_type == 'LIVINGSPACE':
                room = LivingSpace(room_name.upper(), room_type.upper())

                self.rooms.append(room)
                self.livingspaces.append(room)
                self.vacant_livingspaces.append(room)
                print('Room created successfully')
                return 'Room created successfully'
            else:
                return 'room type can only be an office or livingspace'
        else:
            return 'Invalid Input'

    def reallocate_person(self, first_name, last_name, room_name):
        """ reallocate a person to a new vacant room"""

        # list comprehension which check if the person exist
        person = [person for person in self.persons
                  if person.first_name.upper() == first_name.upper() and
                  person.last_name.upper() == last_name.upper()]

        # list comprehension which check if the new room exist
        new_room = [new_room for new_room in self.rooms
                    if new_room.room_name.upper() == room_name.upper()]
        if not person:
            return 'Person does not exist'

        elif not new_room:
            return 'the new room does not exist'

        # check if the person is an occupant of the new room
        elif [occupant for occupant in new_room[0].occupants
              if occupant.first_name.upper() == first_name.upper() and
              occupant.last_name.upper() == last_name.upper()]:
            return 'you cannot be reallocated to the same room'

        # check the vacancy of the room
        elif new_room[0].room_type == 'OFFICE' and len(new_room[0].occupants) is new_room[0].limit:
            return 'The office has no vacancy'

        elif new_room[0].room_type == 'LIVINGSPACE' and len(new_room[0].occupants) is new_room[0].limit:
            return 'The livingspace has no vacancy'

        # reallocate person to the new room ofthe same room type
        else:
            room = [room for room in self.rooms if person[0] in room.occupants]
            if room:
                if room[0].room_type == new_room[0].room_type:
                    new_room[0].occupants.append(person[0])
                    room[0].occupants.remove(person[0])
                    return'You have been reallocated to a new room'
                else:
                    return 'You can only be reallocated to the same room_type'
            else:
                return 'person not allocated'

    def load_people(self, file_name):
        """Method which loads people from a text file to amity system """
        try:
            with open(file_name, 'r') as f:
                people = f.readlines()
                if people:
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
                            self.add_person(first_name, last_name,
                                            job_type, want_accomodation)
                            print ('Adding people from the txt file successful')
                else:
                    return 'file is empty'
        except IOError:
            return 'file not found'

    def print_allocations(self, file_name):
        output = ''
        # check the room name and type from the room list
        for room in self.rooms:
            output += room.room_name + room.room_type + '\n'
            output += '-' * 80 + '\n'
            if room.occupants:
                output += ', '.join(person.first_name + '  ' +
                                    person.last_name for person in room.occupants) + '\n'
            else:
                output += 'This room is empty.\n'
        print output

        # save the allocations of a text file
        if file_name:
            with open(file_name, 'w') as f:
                f.write(output)
                print ('Allocations have been saved to the file: \n')
                return 'Allocations have been saved to the file: \n'

    def print_unallocated(self, file_name):
        """ prints unallocated people on the screen and saves to a text file """
        output = ''
        output += '-' * 50 +'\n'
        output += 'Unallocated to offices' + '\n'
        output += '-' * 50 + '\n'
        for person in self.persons:
            if person in self.unallocated_persons:
                output += (person.first_name + '  ' + person.last_name) + '\n'
        output += '-' * 50 + '\n'
        output += 'Unallocated to livingspaces' + '\n'
        output += '-' * 50 + '\n'
        for person in self.persons:
            if person in self.unaccomodated_fellows:
                output += (person.first_name + '  ' + person.last_name) + '\n'
        print output

        if file_name:
            with open(file_name, 'w') as f:
                f.write(output)
                print ('Unallocated people have been saved to the file: \n')
                return 'Unallocated people have been saved to the file: \n'

    def print_room(self, room_name):
        """Print the occupants of the room on the screen"""
        if room_name.upper() not in [room.room_name.upper() for room in self.rooms]:
            print ('The room is not available')
        for room in self.rooms:
            if room.room_name.upper() == room_name.upper():
                print (room.room_name + '-' + room.room_type)
                print ('-' * 80)
                if room.occupants:
                    for person in room.occupants:
                        print (person.first_name + " " +
                               person.last_name + " " + person.job_type)
                else:
                    print ('this room has no occupants')

    def save_state(self, db_name='database.db'):
        """
        Save all application data to the database 'database.db',
        or optionally, a user-defined database 
        """

        if db_name:
            engine = create_engine('sqlite:///{}'.format(db_name))
        else:
            engine=create_engine('sqlite:///database.db')
       
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for person in self.persons:
            person = Person(id=None, first_name=person.first_name,
                            last_name=person.last_name, job_type=person.job_type, want_accomodation=person.want_accomodation)
            session.add(person)
            session.commit()

        for room in self.rooms:
            room = Room(id=None, room_name=room.room_name,
                        room_type=room.room_type)
            session.add(room)
            session.commit()
        session.close()

    def load_state(self, db_name):
        """ loads data from a user defined database to the application """

        engine = create_engine('sqlite:///{}'.format(db_name))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for first_name, last_name, job_type, want_accomodation in session.query(Person.first_name, Person.last_name, Person.job_type, Person.want_accomodation):
            if job_type == 'staff':
                person = Staff(first_name, last_name,
                               job_type, want_accomodation)
                self.persons.append(person)
                self.staffs.append(person)
                self.unallocated_persons.append(person)

            else:
                person = Fellow(first_name, last_name,
                                job_type, want_accomodation)
                self.persons.append(person)
                self.fellows.append(person)
                self.unaccomodated_fellows.append(person)

        for room_name, room_type in session.query(Room.room_name, Room.room_type):
            if room_type == 'office':
                room = Office(room_name, room_type)
                self.rooms.append(room)
                self.offices.append(room)
            else:
                room = LivingSpace(room_name, room_type)
                self.rooms.append(room)
                self.livingspaces.append(room)
