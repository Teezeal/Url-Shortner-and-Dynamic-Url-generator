from .models import Urls
import random
import string

def generate_short_url(instance):
    """Generates a random 6-character string for the short URL."""
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    while Urls.objects.filter(short_url=short_url).exists():
        short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url