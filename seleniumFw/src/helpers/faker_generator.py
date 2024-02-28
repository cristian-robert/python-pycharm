from faker import Faker

class FakerGenerator:
    def __init__(self):
        self.faker = Faker()

    def name(self):
        return self.faker.name()

    def email(self):
        return self.faker.email()

    def address(self):
        return self.faker.address()

