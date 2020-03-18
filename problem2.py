import sys
import re
def process(front,back):
    if not front and back: return '/'
    if not front: return back if back[0] == '/' else '/' + back
    if back[0] != '/':
        back = '/' + back
    url = front + back
    url = re.sub(r'//','/',url)
    return url

for line in sys.stdin:
    line = line.replace('\n','')
    lists = line.split(',')
    front = lists[0]
    back = lists[1]
    res = process(front,back)
    print(res)

if __name__ == "__main__":
    line = '/a/,b/'
    line = line.replace('\n','')
    lists = line.split(',')
    front = lists[0]
    back = lists[1]
    res = process(front,back)
    print(res)
