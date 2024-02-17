class Restaurant():
    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("O nome do restaurante é " + self.restaurant_name.title() + ".")
        print("E seu tipo de cozinha é " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " está aberto!")

    def set_number_served(self, clients):
        self.number_served = clients

    def increment_number_served(self, clients):
        self.number_served += clients
