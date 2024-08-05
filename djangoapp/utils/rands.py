from random import SystemRandom
from django.utils.text import slugify
import string


def random_letter(k):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits, k=k
    ))


def slugify_new(text, k: int):
    return slugify(text) + '-' + random_letter(k)
