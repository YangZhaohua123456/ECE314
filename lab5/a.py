#import string as sn
#translator = str.maketrans('', '', sn.punctuation)
#st='just,do:it'
#print(st.translate(translator))
#print("sfafae".split)
f = open('documentA.txt','r')
for i in f :
    print(type(i))
    print(i.split())
    print(i)