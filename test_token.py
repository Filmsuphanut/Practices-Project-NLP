import warnings
import pythainlp
from pythainlp import sent_tokenize, word_tokenize


f = open("ab.txt", "r",encoding='utf-8')
text = f.read()


text = "เมืองเชียงรายมีประวัติศาสตร์อันยาวนาน        เป็นที่ตั้งของหิรัญนครเงินยางเชียงแสน"

# print("sent_tokenize:", sent_tokenize(text))
# print("word_tokenize:", word_tokenize(text))
# print("no whitespace:", word_tokenize(text, keep_whitespace=False))

# print("newmm    :", word_tokenize(text))  # default engine is "newmm"
# print("longest  :", word_tokenize(text, engine="longest"))
# print("multi_cut:", word_tokenize(text, engine="multi_cut"))


print("deepcut  :", word_tokenize(text, engine="deepcut", keep_whitespace=False))

#print("pyicu    :", word_tokenize(text, engine="pyicu"))
#print("tcc      :", word_tokenize(text, engine="tcc"))
#print("etcc     :", word_tokenize(text, engine="etcc"))
#print("ulmfit   :", word_tokenize(text, engine="ulmfit"))