# 코멘토 직무부트캠프 과제 1
# adddata.py

f = open("새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
