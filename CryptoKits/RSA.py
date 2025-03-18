from Crypto.Util.number import long_to_bytes

def dpdq_leak(p, q, dp, dq, c):
    """
    dp,dq泄露
    """
    mp = pow(c,dp,p)
    mq = pow(c,dq,q)
    pi = pow(p, -1, q)
    m = ((((mq-mp)*pi)%q)*p+mp)%(p*q)
    
    return long_to_bytes(m)

def dp_leak(dp, e, n, c):
    a = dp*e-1
    for x in range(2,e):
        if a%x == 0:
            p = a//x+1
            if n%p == 0:
                q = n//p
                break
    d = pow(e,-1,(p-1)*(q-1))
    m = pow(c,d,n)
    return long_to_bytes(m)