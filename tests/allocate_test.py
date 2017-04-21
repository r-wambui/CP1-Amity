import unittest
from CP1.allocate import Amity


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_add_person(self):
        """
        People can be added to Amity system """
        self.assertEqual(self.amity.add_person(
            'Rose', 'Wambui', 'Fellow', 'Y'), 'Person added successfully')

    def test_create_room(self):
        """
        Rooms can be created """
        self.assertEqual(self.amity.create_room(
            'Vanhalla', 'LivingSpace'), 'Room created successfully')

    def test_allocate_person(self):
        self.amity.create_room('Java', 'LivingSpace')
        self.amity.add_person('Rose', 'Wambui', 'Fellow', 'Y')

        self.assertEqual(self.amity.allocate_person(
            'Rose', 'Wambui', 'Fellow', 'Java'),
            'Person allocated successfully')

    def test_reallocate_a_person(self):
        self.amity.create_room('Cairo', 'office')
        self.amity.create_room('Asmara', 'office')
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
