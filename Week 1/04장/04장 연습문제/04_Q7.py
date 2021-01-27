f = open("test3.txt", 'r')
text = f.read()
f.close()

text = text.replace('java', 'python')

f = open('test3.txt','w')
f.write(text)
f.close()
