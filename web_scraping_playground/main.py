from hackernews import get_response, greater_than_hundred

greater_than_hundred(get_response())
answer = input('want more?')
if answer.upper() == 'Y' or answer.upper() == 'YES':
    greater_than_hundred(get_response('https://news.ycombinator.com/news?p=2'))
else:
    print("Done!")
