from server import db
from server.models import Users, Snippets, Snippets_Keywords, Keywords
from server.db_engine.seed_data import users, snippets, snippets_keywords, keywords

MODELS = [Users, Snippets, Snippets_Keywords, Keywords]
db.bind(MODELS, bind_refs=False, bind_backrefs=False)
db.connect()

db.drop_tables([Snippets_Keywords, Keywords, Users, Snippets])
db.create_tables([Users, Snippets, Keywords, Snippets_Keywords])


# Users 1 - Snippets with odd IDs
# Users 2 - Snippets with even IDs
Users.insert_many(users).execute()

Snippets.insert_many(snippets).execute()

keywords = Keywords.insert_many(keywords).returning(Keywords).execute()


# Maintaining many-to-many relationship b/w snippets/keywords
snippets = (
    Snippets_Keywords.insert_many(snippets_keywords)
    .returning(Snippets_Keywords)
    .execute()
)

snippet = Snippets.get(Snippets.id == 1).to_dict()

keywords = (
    Keywords.select()
    .join(Snippets_Keywords, on=Keywords.id == Snippets_Keywords.keyword_id)
    .where(Snippets_Keywords.snippet_id == 1)
)

keywords_list = []
for word in keywords:
    keywords_list.append(word.to_dict())

snippet["keywords"] = keywords_list

print(snippet)

db.close()
