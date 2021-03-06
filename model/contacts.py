from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.email = email
        self.home = home
        self.id = id


    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)


    def __eq__(self, another):
        return (self.id is None or another.id is None or self.id == another.id) and self.firstname == another.firstname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize