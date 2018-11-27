import requests
from server.config import Config
from .MOCK_DATA import data


def decorate_keywords_with_images(keywords):
    results = []
    for keyword in keywords:
        unsplash = _search_unsplash_by_keyword(keyword)
        images = _extract_images(unsplash)
        results.append(
            {
                "keyword": keyword,
                "images": images,
                "meta": {
                    "total_images": unsplash["total"],
                    "total_pages": unsplash["total_pages"],
                    "last_page": 1,
                },
            }
        )
    return results


MOCK_DATA = data

BASE_URL = "https://api.unsplash.com/search/photos/"
CLIENT_ID = Config.UNSPLASH_CLIENT_ID


def _search_unsplash_by_keyword(keyword, page=1, per_page=15):
    query_params = {
        "query": keyword,
        "page": page,
        "per_page": per_page,
        # "orientation":
        "client_id": CLIENT_ID,
    }

    # --- REAL RESPONSE ---
    res = requests.get(url=BASE_URL, params=query_params)
    data = res.json()

    # data = MOCK_DATA

    return data


def _extract_images(unsplash):
    """
    Clean each raw Unsplash image result to fit desired data model:
    {
        id,
        description,
        thumb,
        regular,
        source,
        author: {
            name,
            page
        }
    }
    """
    results = []
    for image in unsplash["results"]:
        output = {}
        output["id"] = image["id"]
        output["description"] = image["description"]
        output["thumb"] = image["urls"]["thumb"]
        output["regular"] = image["urls"]["regular"]
        output["source"] = image["links"]["html"]
        output["author"] = {}
        if "name" in image["user"]:
            output["author"]["name"] = image["user"]["name"]
        if "html" in image["user"]["links"]:
            output["author"]["page"] = image["user"]["links"]["html"]
        results.append(output)
    return results
