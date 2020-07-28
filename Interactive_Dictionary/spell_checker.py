from spellchecker import SpellChecker

def get_correct(word):
    if not word or isinstance(word,bool):
        return None

    spell = SpellChecker()
    result = spell.candidates(word)
    if spell.correction(word) == word:
        return None
    else:
        return result

print(get_correct('shaghdshahdhjdhjjhad'))
print(get_correct(None))
print(get_correct(True))
print(get_correct('tigr'))


