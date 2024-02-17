from users import User

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Lista de privilégios:")
        for privilege in self.privileges:
            print("\t" + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges(
            privileges=['can add post', 'can delete post', 'can ban user'])
