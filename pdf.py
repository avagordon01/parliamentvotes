import textract

import unicodedata, re, itertools, sys

all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc'}
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) in categories)
control_char_re = re.compile('[' + re.escape(control_chars) + ']')

def remove_control_chars(s):
    return control_char_re.sub('\n', s)

def extract_text_from_pdf(filename):
    return remove_control_chars(textract.process(filename).decode('utf-8'))
