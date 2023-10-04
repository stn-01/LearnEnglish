vowels_short = ['e', 'æ', 'ʌ', 'ʊ', 'ɒ', 'ə', 'ɪ'] # ɪ
vowels_long = ['i:', 'ɜ:', 'ɔ:', 'u:', 'ɑ:']
vowels_diphthong = ['ɪə', 'eə', 'eɪ', 'ɔɪ', 'aɪ', 'əʊ', 'aʊ']

consonants_fricatives = ['f', 'v', 'θ', 'ð', 'z', 'ʃ', 'ʒ', 'h', 's'] # s
consonants_plosives = ['p', 'b', 't', 'd', 'k', 'g']
consonants_affricates = ['ʈʃ', 'dʒ']
consonants_nasals = ['m', 'n', 'ŋ']
consonants_approximants = ['r', 'j', 'w', 'l']

ALPHABET = {
    'a': {'name': 'eɪ', 'char_upper': 'A', 'char_lower': 'a', 'sound': '[eɪ] / [æ]', 'alphabet_sound': 'eɪ', 'short_sound': 'æ',},
    'e': {'name': 'i:', 'char_upper': 'E', 'char_lower': 'e', 'sound': '[i:] / [e]', 'alphabet_sound': 'i:', 'short_sound': 'e'},
    'i': {'name': 'aɪ', 'char_upper': 'I', 'char_lower': 'i', 'sound': '[aɪ] / [ɪ]', 'alphabet_sound': 'aɪ', 'short_sound': 'ɪ'},
    'y': {'name': 'waɪ', 'char_upper': 'Y', 'char_lower': 'y', 'sound': '[aɪ] / [ɪ] / [j]', 'alphabet_sound': 'aɪ', 'short_sound': 'ɪ'},
    'o': {'name': 'əʊ', 'char_upper': 'O', 'char_lower': 'o', 'sound': '[əʊ] / [ɒ]', 'alphabet_sound': 'əʊ', 'short_sound': 'ɒ'},
    'u': {'name': 'ju:', 'char_upper': 'U', 'char_lower': 'u', 'sound': '[ju:] / [ʌ]', 'alphabet_sound': 'ju:', 'short_sound': 'ʌ'},

    't': {'name': 'ti:', 'char_upper': 'T', 'char_lower': 't', 'sound': '[t]'},
    'd': {'name': 'di:', 'char_upper': 'D', 'char_lower': 'd', 'sound': '[d]'},
    'n': {'name': 'en', 'char_upper': 'N', 'char_lower': 'n', 'sound': '[n]'},
    'l': {'name': 'el', 'char_upper': 'L', 'char_lower': 'l', 'sound': '[l]'},
    's': {'name': 'es', 'char_upper': 'S', 'char_lower': 's', 'sound': '[s]'},
    'z': {'name': 'zed', 'char_upper': 'Z', 'char_lower': 'z', 'sound': '[z]'},

    'k': {'name': 'keɪ', 'char_upper': 'K', 'char_lower': 'k', 'sound': '[k]'},
    'g': {'name': 'dʒi:', 'char_upper': 'G', 'char_lower': 'g', 'sound': '[g] / [dʒ]'},

    'p': {'name': 'pi:', 'char_upper': 'P', 'char_lower': 'p', 'sound': '[p]'},
    'b': {'name': 'bi:', 'char_upper': 'B', 'char_lower': 'b', 'sound': '[b]'},
    'm': {'name': 'em', 'char_upper': 'M', 'char_lower': 'm', 'sound': '[m]'},
    'w': {'name': 'dʌblju:', 'char_upper': 'W', 'char_lower': 'w', 'sound': '[w]'},

    'f': {'name': 'ef', 'char_upper': 'F', 'char_lower': 'f', 'sound': '[f]'},
    'v': {'name': 'vi:', 'char_upper': 'V', 'char_lower': 'v', 'sound': '[v]'},

    'r': {'name': 'ɑ:r', 'char_upper': 'R', 'char_lower': 'r', 'sound': '[r]'},
    'c': {'name': 'si:', 'char_upper': 'C', 'char_lower': 'c', 'sound': '[s] / [k]'},

    'j': {'name': 'dʒeɪ', 'char_upper': 'J', 'char_lower': 'j', 'sound': '[dʒ]'},

    'q': {'name': 'kju:', 'char_upper': 'Q', 'char_lower': 'q', 'sound': '[kw]'},

    'h': {'name': 'eɪʈʃ', 'char_upper': 'H', 'char_lower': 'h', 'sound': '[h]'},
    'x': {'name': 'eks', 'char_upper': 'X', 'char_lower': 'x', 'sound': '[ks] / [gz]'},
}
