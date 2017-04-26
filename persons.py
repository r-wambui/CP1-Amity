class Person(object):

    def __init__(self, fname=None, lname=None, role=None, want_accomondation=None):
        self.fname = fname
        self.lname = lname
        self.role = role
        self.want_accomondation = want_accomondation


class Fellow(Person):

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class Staff(Person):

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
