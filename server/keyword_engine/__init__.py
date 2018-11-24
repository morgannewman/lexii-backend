from .language_processing import generate_raw_keywords
from .unsplash import decorate_keywords_with_images


def generate_keywords(title, content):
    raw_keywords = generate_raw_keywords(title, content)
    return decorate_keywords_with_images(raw_keywords)


def store_keywords(snippet_id, decorated_keywords):
    return "this should store the keywords in DB"
