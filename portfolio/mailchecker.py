import requests
import json

def check_mail_valid(email):
    email = str(email)
    result = requests.get(f"https://disposable.debounce.io/?email={email}").text
    if 'error' in result:
        return None
    elif 'disposable' in result:
        result = json.loads(requests.get(f"https://disposable.debounce.io/?email={email}").text)['disposable']

    if result == 'true':
        return True
    elif result == 'false':
        return False
