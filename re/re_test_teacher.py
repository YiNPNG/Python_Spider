import re
import sys

port = sys.argv[1]

f = open('1.txt')
while True:
    data = ''
    for i in f:
        if i != '\n':
            data += i
        else:
            break
    
    if not data:
        print('no port')
        break

    # 获取每段首单词
    try:
        PORT = re.match(r'\S+',data).group()
    except Exception:
        continue
    if PORT == port:
        # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        pattern = r'([0-9]{1,3}\.){3}[0-9]{1,3}/\d+|Unknown'
        address = re.search(pattern,data).group()
        print(address)
        break

f.close() 