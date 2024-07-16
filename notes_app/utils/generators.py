import random
import string


class Generators:
    def generate_random_str(self):
        chars = self.char_len_generator()
        name = string.ascii_letters
        return ''.join(random.choice(name) for i in range(chars))

    def generate_mixed_str(self):
        chars = self.char_len_generator()
        final_str = string.ascii_letters + string.digits
        return ''.join(random.choice(final_str) for i in range(chars))

    def char_len_generator(self):
        return random.randint(8, 15)
