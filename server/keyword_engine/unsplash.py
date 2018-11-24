import requests
from server.config import Config
from server.helpers import generate_utcnow_str
from flask import json
from . import MOCK_DATA

MOCK_DATA = json.loads(MOCK_DATA)

BASE_URL = "https://api.unsplash.com/search/photos/"
CLIENT_ID = Config.UNSPLASH_CLIENT_ID
CLIENT_SECRET = Config.UNSPLASH_CLIENT_SECRET


def search_unsplash_by_keyword(keyword, page=1, per_page=10):
    query_params = {
        "query": keyword,
        "page": page,
        "per_page": per_page,
        # "orientation":
        "client_id": CLIENT_ID,
    }

    # --- REAL RESPONSE ---
    # res = requests.get(url=BASE_URL, params=query_params)
    # data = res.json()

    data = MOCK_DATA

    # l = len(data["results"])
    # dicts = []
    # for i in range(l):
    #     d = {}
    #     d["id"] = data["results"][i]["id"]
    #     d["description"] = data["results"][i]["description"]
    #     d["thumb"] = data["results"][i]["urls"]["thumb"]
    #     d["regular"] = data["results"][i]["urls"]["regular"]
    #     d["links"] = {}
    #     if (
    #         "links" in data["results"][i]["user"]
    #         and "html" in data["results"][i]["user"]["links"]
    #     ):
    #         d["links"]["html"] = data["results"][i]["links"]["html"]
    #     d["user"] = {}
    #     if "username" in data["results"][i]["user"]:
    #         d["user"]["username"] = data["results"][i]["user"]["username"]
    #     if "portfolio_url" in data["results"][i]["user"]:
    #         d["user"]["portfolio_url"] = data["results"][i]["user"]["portfolio_url"]
    #         # json_d = json.dumps(d)
    #     dicts.append(d)
    return data


def decorate_keywords_with_images(keywords):
    result = []
    for item in keywords:
        result.append(
            {
                "keyword": item["keyword"], 
                "images": search_unsplash_by_keyword(item["keyword"]),
                "meta": {
                    "total_images": "",
                    ""
                }
                "updated_at": generate_utcnow_str(),
                "created_at": item["created_at"]
            }
        )
    return result
