from typing import Optional
import requests
from bs4 import BeautifulSoup


def get_response(url='https://news.ycombinator.com/news'):
    result = requests.get(url)
    if result.status_code != 200:
        return None
    else:
        soup = BeautifulSoup(result.text, 'html.parser')
        scores = soup.select('.score')
        title = soup.select('.storylink')
    return [scores, title]


def greater_than_hundred(response: get_response()) -> object:
    """
    Checks if the response got is valid and works upon it to give valid results
    with points greater than 100
    :rtype: str

    """
    try:
        for index, score in enumerate(response[0]):
            point = int(score.string.replace(' points', ''))
            if point > 100:
                print(f"title: {response[1][index].string}")
                print(f"link: {response[1][index].get('href')}")
                print(f"points: {point}")
                print()
    except (TypeError, AttributeError):
        return 'We encountered a problem, Please check your internet connection and link.'
