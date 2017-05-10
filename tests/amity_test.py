import unittest

from models.amity import Amity


class AmityTest(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_add_person(self):
        """
        People can be added to Amity system """
        self.assertEqual(self.amity.add_person(
            'Rose', 'Wambui', 'Fellow', 'Y'), 'Person added successfully')

    def test_add_person_already_exist(self):
        self.amity.add_person('rose', 'wambui', 'fellow', 'Y')
        self.assertEqual(self.amity.add_person('rose', 'wambui', 'fellow', 'Y'), 'Person already Exists')

    def test_add_person_can_only_be_staff_or_fellow(self):
        """
        Only people with the role of a fellow or staff can be added to amity system"""
        self.assertEqual(self.amity.add_person(
            'Rose', 'Wambui', 'visitor', 'N'),
            'The person role can only be a staff or a fellow')

    def test_add_person_name_can_only_be_string(self):     
        self.assertEqual(self.amity.add_person(
                          6, 'Wambui', 'Fellow', 'Y'), 'Invalid input')

    def test_add_person_job_type_can_only_be_string(self):
        self.assertEqual(self.amity.add_person(
                          'Rose', 'Wambui', 8, 'Y'), 'Invalid input')

    def test_add_person_staff_cannot_be_allocated_livingspace(self):
        """ A person whose role is a staff cannot be allocated to livingspace"""
        self.assertEqual(self.amity.add_person(
            'Rose', 'Wambui', 'Staff', 'Y'),
            'A staff cannot be allocated a living space')

    def test_create_room(self):
        """
        Rooms can be created """
        self.assertEqual(self.amity.create_room(
            'Vanhalla', 'LivingSpace'), 'Room created successfully')

    def test_create_room_cannot_create_existing_room(self):
        self.amity.create_room('Cairo', 'Office')
        self.assertEqual(self.amity.create_room('Cairo', 'Office'), 'Room already created')

    def test_create_room_room_name_is_a_string(self):
        self.assertEqual(self.amity.create_room(4, 'LivingSpace'), 'Invalid Input')

    def test_create_room_type_is_a_string(self):
        self.assertEqual(self.amity.create_room('Ruby', 9), 'Invalid Input')

    def test_allocate_livingspace_can_only_accomodate_a_max_of_4(self):
        self.amity.create_room('Ruby', 'LivingSpace')
        self.amity.add_person('Winne', 'Mumbi', 'Fellow', 'Y')
        self.amity.add_person('Rose', 'Wambui', 'Fellow', 'Y')
        self.amity.add_person('Joan', 'Awinja', 'Fellow', 'Y')
        self.amity.add_person('Winne', 'Mumbi', 'Fellow', 'Y')

        self.amity.add_person('Julie', 'Wanja', 'Fellow', 'Y')
        self.assertEqual(self.amity.allocate_livingspace(
            'Julie', 'Wanja', 'Fellow', 'Ruby'),
            'This room can only accomodate 4 people')

    def test_allocate_office_can_only_accomodate_a_max_of_6(self):
        self.amity.create_room('Round Table', 'Ofice')
        self.amity.add_person('Winne', 'Mumbi', 'Fellow', 'Y')
        self.amity.add_person('Rose', 'Wambui', 'Fellow', 'N')
        self.amity.add_person('Joan', 'Awinja', 'Fellow', 'Y')
        self.amity.add_person('Winne', 'Mumbi', 'Fellow', 'N')
        self.amity.add_person('James', 'Oscar', 'Staff', 'N')
        self.amity.add_person('Shem', 'Nashon', 'Staff', 'N')

        self.amity.add_person('Julie', 'Wanja', 'Fellow', 'Y')
        self.assertEqual(self.amity.allocate_office(
            'Julie', 'Wanja', 'Fellow', 'Round Table'),
            'An office can only have a maximum of 6 people')

    def test_reallocate_a_person(self):
        """
        A person can move from one room to another """
        self.amity.create_room('Cairo', 'office')
        self.amity.add_person('Rose', 'Wambui', 'Fellow', 'N')

        self.amity.create_room('Asmara', 'Office')

        self.assertEqual(self.amity.reallocate_person(
            'Rose', 'Wambui', 'Fellow', 'Asmara'),
            'You have been reallocated to a new room')


    def test_print_allocations(self):
        self.amity.create_room('Accra', 'Office')
        self.amity.add_person('Rose', 'Wambui', 'Fellow', 'N')
        self.amity.add_person('Joan', 'Awinja', 'Fellow', 'Y')
        self.amity.allocate_person('Rose', 'Wambui', 'Fellow', 'Round Table')
        self.amity.allocate_person('Joan', 'Awinja', 'Fellow', 'Round Table')
        self.assertEqual(self.amity.print_allocations(),
                         'Allocations printed successfully')

    def test_print_unallocated(self):
        self.amity.create_room('Accra', 'Office')
        self.amity.add_person('Rose', 'wambui', 'Fellow', 'Y')
        self.assertEqual(self.amity.print_unallocated(),
                         'Printed a list of unallocate people')

    def test_save_state(self):
        self.assertEqual(self.amity.save_state(
            'allocate_db'), 'Saved successfully')

    def test_load_state(self):
        self.assertEqual(self.amity.load_state(
            'allocate_db'), 'data loaded successfully')
