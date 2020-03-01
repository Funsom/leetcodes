def pows(x,n):
    if n > 0:
        if n == 2:
            return x*x
        if n % 2 == 0:
            res = pows(x,n//2)
            return res * res
        else:
            n -= 1
            res = pow(x,n//2)
            return res * res * x
    elif n < 0:
        if n == -2:
            return 1 / x / x
        if n % 2 == 0:
            res = pows(x,n//2)
            return res * res
        else:
            n += 1
            res = pow(x,n//2)
            return res * res / x
    else:
        return 1

if __name__ == "__main__":
    print(pows(2,0))