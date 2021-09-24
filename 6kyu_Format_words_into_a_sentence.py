"""
Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. Empty string values should be ignored. Empty arrays or null/nil values being passed into the method should result in an empty string being returned.

format_words(['ninja', 'samurai', 'ronin']) # should return "ninja, samurai and ronin"
format_words(['ninja', '', 'ronin']) # should return "ninja and ronin"
format_words([]) # should return ""

"""


def format_words(words):
    if not words:
        return ''
    elif len(words) == 1:
        return words[0]
    words = [i for i in words if i != '']
    if len(words) == 1:
        return words[0]

    return ', '.join(words[:-1]) + ' and ' + words[-1]
