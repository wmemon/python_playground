import requests
import json


def get_result(word):
    # Requests module and filter json file
    result = requests.get(f'https://api.dictionaryapi.dev/api/v1/entries/en/{word}')
    if result.status_code == 200:
        return result
    else:
        return None


def get_meaning(result):
    if not result:
        return "No search result found."
    # Storing meaning in a list format
    meaning = []

    result_sep = json.loads(result.text)[0].get('meaning')
    for _ in result_sep.keys():
        meaning.append(f"{_} : {result_sep.get(_)[0].get('definition')}")

    return meaning

def get_example(result):
    if not result:
        return "No example found."
    # Storing example in a list format
    example = []

    result_sep = json.loads(result.text)[0].get('meaning')

    for _ in result_sep.keys():
        if not result_sep.get(_)[0].get('example'):
            continue
        example.append(f"{_} : {result_sep.get(_)[0].get('example')}")
    if not example:
        return "Example not found!"
    return example


# print(get_result(None))
# print(get_result(True))
#print(get_result('lAmBdA').text)