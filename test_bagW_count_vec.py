from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from pythainlp import sent_tokenize, word_tokenize


def count_vec(data1):
    cvec = CountVectorizer(analyzer=lambda x:x.split(','))
    cv = cvec.fit_transform(data1)
    return cv

def Tfidf_vec(data1):
    tvec = TfidfVectorizer(analyzer=lambda x:x.split(','),)
    tv = tvec.fit_transform(data1)
    return tv