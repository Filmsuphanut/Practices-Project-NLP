from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from pythainlp import sent_tokenize, word_tokenize

f = open("text.txt", "r",encoding='utf-8')
text1 = f.read()
#f = open("text1.txt", "r",encoding='utf-8')
#text2 = f.read()


data1 = word_tokenize(text1, engine="deepcut", keep_whitespace=False)
#data2 = word_tokenize(text2, engine="deepcut", keep_whitespace=False)
#data = [data1,data2]

#tokens_list_j = [','.join(tkn) for tkn in data]

cvec = CountVectorizer(analyzer=lambda x:x.split(','))
c_feat = cvec.fit_transform(data1)


print(cvec.vocabulary_) #ดูคำ
print(c_feat)
#print(c_feat.todense()) #เทียบกัน 0 - 20

# tvec = TfidfVectorizer(analyzer=lambda x:x.split(','),)
# t_feat = tvec.fit_transform(tokens_list_j)

# print(t_feat) #ดูคำ
# print(t_feat[:,:5].todense())