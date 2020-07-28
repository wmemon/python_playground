import paralleldots

paralleldots.set_api_key("SAZPfO9Nuk1jQrWD66i9oqTpTHr9wqaFlqkQJVNV45E")
text = "This is a sunny morning!"
# print(paralleldots.sentiment(text,"en"))
lang_text = "C'est un environnement très hostile, si vous choisissez de débattre ici, vous serez vicieusement attaqué par l'opposition."
lang_code = "fr"
category  = { "finance": [ "markets", "economy", "shares" ], "world politics": [ "diplomacy", "UN", "war" ], "india": [ "congress", "india", "bjp" ] }
print(paralleldots.emotion(text))
