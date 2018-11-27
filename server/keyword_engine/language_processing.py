import re

import requests
from server.config import Config


def generate_raw_keywords(title, content):
    # construct document object to interact with Google API
    document = title + " " + content
    # make two API calls to generate keywords
    keywords = _fetchEntities(document)
    category = _fetchCategory(document)
    return [category] + keywords


def _fetchEntities(document):
    _ENTITIES_API = "https://language.googleapis.com/v1/documents:analyzeEntities"
    req = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": document
        }
    }
    res = requests.post(url=_ENTITIES_API, params={"key": Config.GOOGLE_CLOUD_API_KEY}, json=req)
    response = res.json()
    print("entities", response)
    return _extractKeywords(res.json()["entities"])


def _fetchCategory(document):
    _CATEGORIES_API = "https://language.googleapis.com/v1/documents:classifyText"
    req = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": document
        }
    }
    res = requests.post(url=_CATEGORIES_API, params={"key": Config.GOOGLE_CLOUD_API_KEY}, json=req)
    response = res.json()
    print("categories", response)
    return _extractClassification(res.json()["categories"])


def _extractKeywords(data):
    maxWords = 3
    result = []
    count = 0
    for entity in data:
        if count == maxWords:
            break
        result.append(entity["name"])
        count += 1

    return result


def _extractClassification(data):
    """
    EXAMPLE RAW INPUT:
    /Internet & Telecom/Email & Messaging/Text & Instant Messaging
    """
    raw = data[0]["name"]
    # Split by slash characters
    categories = re.split(r"\/(.*?)", raw)
    # Return the last item in the category list, since it's the most specific
    return categories[-1]
