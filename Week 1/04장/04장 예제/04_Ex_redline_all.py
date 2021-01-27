# 코멘토 직무부트캠프 과제 1
# readline_all.py

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
