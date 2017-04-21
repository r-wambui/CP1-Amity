class Person(object):

    def __init__(self, fname, lname, role, want_accomondation):
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
        self.lname = lnmae
