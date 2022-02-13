from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from pythainlp import sent_tokenize, word_tokenize

f = open("ab.txt", "r",encoding='utf-8')
text1 = f.read()
o = open("te.txt", "r",encoding='utf-8')
text2 = o.read()


aa = word_tokenize(text1, engine="deepcut", keep_whitespace=False)
bb = word_tokenize(text2, engine="deepcut", keep_whitespace=False)
data = [aa,bb]

tokens_list_j = [','.join(tkn) for tkn in data]

cvec = CountVectorizer(analyzer=lambda x:x.split(','))
c_feat = cvec.fit_transform(tokens_list_j)


print(cvec.vocabulary_) #ดูคำ
# print(c_feat.shape) #ดูคำ
# print(c_feat.todense()) #ดูคำ

# tvec = TfidfVectorizer(analyzer=lambda x:x.split(','),)
# t_feat = tvec.fit_transform(tokens_list_j)

# print(t_feat) #ดูคำ
# print(t_feat[:,:5].todense())