'''
    Выделите общую часть из двух строк с помошью модуля difflib:
        s1 = u'А роза упала на лапу Азора'
        s2 = u'Дай, Джим, на счастье лапу мне'
'''


from difflib import SequenceMatcher


s1 = u'А роза упала на лапу Азора'
s2 = u'Дай, Джим, на счастье лапу мне'


def main(str1: str, str2: str) -> str:

    sequence_matcher = SequenceMatcher(None, str1, str2)
    longest_match = sequence_matcher.find_longest_match(0, len(str1), 0, len(str2))

    return str1[longest_match.a : longest_match.b]


print(main(s1, s2))
