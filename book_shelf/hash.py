from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.crypto import constant_time_compare
import hashlib

class CustomPasswordHasher(BasePasswordHasher):
    algorithm = "sha2**8-2**5"

    def encode(self, password, salt):
        hash = hashlib.sha224((password + salt).encode()).hexdigest()
        return "%s$%s$%s" % (self.algorithm, salt, hash)

    def verify(self, password, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, salt)
        return constant_time_compare(encoded, encoded_2)

    def safe_summary(self, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        return {
            'algorithm': algorithm,
            'salt': mask_hash(salt),
            'hash': mask_hash(hash),
        }
