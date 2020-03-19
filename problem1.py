import sys
def process(A,B,R):
    res = []
    for x in A:
        nearest = None
        Flag = False
        for y in B:
            if y < x:
                continue
            else:
                if y - x <= R:
                    res.append((x,y))
                    Flag = True
                else:
                    if not nearest and not Flag:
                        nearest = y
                    break
        if nearest:
            res.append((x,nearest))
    return res
if __name__ == "__main__":
    A = [1,3,5]
    B = [2,4,6]
    R = 2
    res = process(A,B,R)
    print(res)
# for line in sys.stdin:
#     line = line.replace('\n','')
#     lists = line.split(r'},')
#     A = lists[0][3:].split(',')
#     A = [int(i) for i in A]
#     B = lists[1][3:].split(',')
#     A = [int(i) for i in B]
#     R = int(lists[2][2:])
#     res = process(A,B,R)
#     output = ""
#     for r in res:
#         output += str(r)
#     print(output)










