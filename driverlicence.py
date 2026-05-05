
class DriverLicence:
    def __init__(self, linumber, lastname, firstname, age, vote, state):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.vote = vote
        self.state = state
        self.linumber = linumber

    def __lt__(self, other ):
        if self.linumber < other.linumber:
            return True
        else:
            return False

    def __gt__(self, other ):
        if self.linumber > other.linumber:
            return True
        else:
            return False

    def __le__(self, other):
        if self.linumber <= other.linumber:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.linumber >= other.linumber:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.linumber == other.linumber:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.linumber != other.linumber:
            return True
        else:
            return False
    def __str__(self):
        output_str = f'{self.linumber}: {self.lastname}, {self.firstname} ({self.age}) {self.vote} in {self.state}'
        return output_str

    def __repr__(self):
        output_str = f'{self.linumber}: ({self.lastname}, {self.firstname} ({self.age}) {self.vote} in {self.state})'
        return output_str
    