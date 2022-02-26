from unicodedata import name


class User:
    def __init__(self, id, name, lastName, userName, password, email):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.userName = userName
        self.password = password
        self.email = email
