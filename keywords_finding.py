# install pymorphy2
# pip install pymorphy2
# pip install -U pymorphy2-dicts-ru
# install nltk
# pip install nltk
import requests as req
import pymorphy2 as morph
from collections import *
import nltk
from nltk import tokenize as tkn
import nltk.corpus as crp


# Accepts: file (https://core.telegram.org/bots/api/#file), bot token, n - Int
# Returns top n keywords
# handler:
# @bot.message_handler(content_types=['document'])
# def handle_docs(message):
#     keywords = find_keywords(bot.get_file(message.document.file_id), settings.keywords_finder_bot_token, 10)
nltk.download("stopwords")
def find_keywords(path, token, n):
    template = "https://api.telegram.org/file/bot{0}/{1}"
    file = req.get(template.format(token, path.file_path))
    text = file.text.encode("ISO-8859-1").decode("utf-8")
    tokenizer = tkn.RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    stopwords = crp.stopwords.words('russian')
    tokens = [i for i in tokens if ( i not in stopwords )]
    analyzer = morph.MorphAnalyzer()
    words = []
    for token in tokens:
        words.append(analyzer.normal_forms(token)[0])
    mosts = [word[0] for word in Counter(words).most_common(n)]
    return mosts
