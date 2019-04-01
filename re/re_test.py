import re
import sys

key = sys.argv[1]
# pattern = r'^(BVI1|BVI101|BVI100|BVI201).*?Internet address is (.*?)\n'
# pattern = r'\b%s .*?Internet address is (.*?)\n'%key
# p = re.compile(pattern,flags=re.S)

# 找对应ＩＰ地址
pattern = r'^%s .*?Internet address is (.*?)\n'%key
p = re.compile(pattern,flags=re.S|re.M)
with open('1.txt','r') as f:
    data = f.read()
    l = p.findall(data)
print(l)

# 找该端口段落
pattern = r'\b%s .*?\n\n'%key
p = re.compile(pattern,flags=re.S)
with open('1.txt','r') as f:
    data = f.read()
    l = p.findall(data)
print(l)