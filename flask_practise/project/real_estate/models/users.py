class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def find_username(self, username) -> bool:
        if self.username == username:
            return True
        return False

    def find_user(self, username, password) -> bool:
        if self.username == username and self.password == password:
            return True
        return False
