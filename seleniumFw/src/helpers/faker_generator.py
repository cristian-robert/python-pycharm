from faker import Faker

class FakerGenerator:
    def __init__(self):
        self.faker = Faker()

    def name(self):
        return self.faker.name()

    def email(self):
        return self.faker.email()

    def address(self):
        return self.faker.street_address()

    def generate_random_string(self, length):
        return self.faker.pystr(min_chars=length, max_chars=length)

    def username(self):
        return self.faker.user_name()

