class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("\nInformações do usuário:\n\tNome: " + self.first_name.title() + " " +
              self.last_name.title() + "\n\tIdade: " + str(self.age) + "\n\tEmail: " + self.email)

    def greet_user(self):
        print("\nOlá " + self.first_name.title() +
              " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
