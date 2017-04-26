import unittest
from CP1_Amity.allocate import Amity
from CP1_Amity.persons import Person
from CP1_Amity.rooms import Room


class AmityTest(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.person = Person()
        self.room = Room()

    def test_add_person(self):
        """
        People can be added to Amity system """

        self.previous_count = len(self.amity.all_person)
        for person in self.amity.all_person:
            self.assertNotIn('Rose', person.fname)
        self.amity.add_person(
            'Rose', 'Wambui', 'Fellow', 'Y')
        self.current_count = len(self.amity.all_person)
        self.assertGreater(self.current_count, self.previous_count)

    def test_create_room(self):
        """
        Rooms can be created """
        self.prevoius_room_count = len(self.amity.all_rooms)
        for room in self.amity.all_rooms:
            self.assertNotIn('Vanhalla', room.name)
        self.amity.create_room(
            'Vanhalla', 'LivingSpace')
        self.current_room_count = len(self.amity.all_rooms)
        self.assertEqual(self.current_room_count - 1, self.prevoius_room_count)

    def test_allocate_person(self):
        """
        A fellow can be allocated to a living space """
        self.previous_allocate_count = len(self.amity.all_allocation)
        self.amity.create_room('Java', 'LivingSpace')
        self.amity.add_person('Rose', 'Wambui', 'Fellow', 'Y')
        self.amity.allocate_person(
            'Rose', 'Wambui', 'Fellow', 'Java')
        self.current_allocate_count = len(self.amity.all_allocation)

        self.assertEqual(self.previous_allocate_count,
                         self.current_allocate_count + 1)

    def test_reallocate_a_person(self):
        """
        A person can move from one room to another """
        self.amity.create_room('Cairo', 'office')
        self.amity.add_person('Rose', 'Wambui', 'Fellow', 'N')
        self.amity.allocate_person('Rose', 'Wambui', 'Fellow', 'Cairo')


        self.assertEqual(self.amity.reallocate_person(
            'Rose', 'Wambui', 'Fellow', 'Asmara'),
            'You have been reallocated to a new room')

    def test_add_person_can_only_be_staff_or_fellow(self):
        self.assertEqual(self.amity.add_person(
            'Rose', 'Wambui', 'CEO', 'N'),
            'The person role can only be a staff or a fellow')

    def test_staff_cannot_be_allocated_a_living_space(self):
        self.assertEqual(self.amity.add_person(
            'Rose', 'Wambui', 'Staff', 'Y'),
            'A staff cannot be allocated a living space')

    def test_add_person_name_and_role_are_both_string(self):
        self.assertRaises(TypeError, self.amity.add_person,
                          6, 'Wambui', 'Fellow', 'Y')
        self.assertRaises(TypeError, self.amity.add_person,
                          'Rose', 'Wambui', 8, 'Y')

    # def test_a_living_space_can_only_accomodate_a_max_of_4(self):

    # def test_an_office_can_only_accomodate_a_max_of_6(self):

    # def test_it_allocates_space_at_random(self):
