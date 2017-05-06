class Person(object):

    def __init__(self, first_name, last_name, job_type, want_accomodation):
        self.first_name = first_name
        self.last_name = last_name
        self.job_type = job_type
        self.want_accomodation = want_accomodation


class Fellow(Person):

    def __init__(self, first_name, last_name, job_type, want_accomodation):
        super(Fellow, self).__init__(first_name, last_name, job_type, want_accomodation)


class Staff(Person):

    def __init__(self, first_name, last_name, job_type, want_accomodation):
        super(Staff, self).__init__(first_name, last_name, job_type, want_accomodation)
