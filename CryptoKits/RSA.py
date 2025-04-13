from Crypto.Util.number import long_to_bytes

from .Util.other import *

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
    """
    dp泄露
    """
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

def common_modulus_attack(n, e1, e2, c1, c2):
    """
    共模攻击
    """
    e1_e2 = e1-e2
    s1 = pow(e1_e2,-1,e2)
    s2 = (1-e1*s1)//e2
    m = pow(c1,s1,n)*pow(c2,s2,n)%n
    return long_to_bytes(m)

def wiener_attack(e, n, c = None):
    """
    Wiener攻击
    满足条件：d < 1/3 * n^0.25
    """
    if not is_sage():
        from sympy import Rational, integer_nthroot
        from sympy.ntheory.continued_fraction import continued_fraction, continued_fraction_convergents
        frac = continued_fraction(Rational(e, n))
        for i in continued_fraction_convergents(frac):
            d, k = i.denominator, i.numerator
            if k == 0:
                continue
            if (e*d-1)%k == 0:
                phi = (e*d-1)//k
                b = n-phi+1
                delta = b*b-4*n
                if delta >= 0 and integer_nthroot(delta, 2)[1]:
                    p = (b+integer_nthroot(delta, 2)[0])//2
                    assert n%p == 0
                    break
        return long_to_bytes(pow(c,d,n)) if c else d
    else:
        from sage.all import continued_fraction
        from sympy import integer_nthroot
        frac = continued_fraction(e/n)
        for i in range(len(frac)):
            d, k = frac.denominator(i), frac.numerator(i)
            if k == 0:
                continue
            if (e*d-1)%k == 0:
                phi = (e*d-1)//k
                b = n-phi+1
                delta = b*b-4*n
                if delta >= 0 and integer_nthroot(delta, 2)[1]:
                    p = (b+integer_nthroot(delta, 2)[0])//2
                    assert n%p == 0
                    break
        return long_to_bytes(int(pow(c,d,n))) if c else d

def extended_wiener_attack(NN, elist, alpha):
    """
    扩展Wiener攻击，通用解法
    Sage脚本，无法import使用，需要手动复制到SageMath中运行
    """
    assert is_sage(), ImportError(f"Error: the function [{inspect.currentframe().f_code.co_name}] is need to run on SageMath.")
    from .Util.sage.RSA.extend_wiener_attack import _attack

    raise EnvironmentError("please check the path to the code and copy it to SageMath and run it")

def extended_wiener_attack_v3(e1, e2, e3, n):
    """
    扩展Wiener攻击，针对三个低解密指数
    Sage脚本，无法import使用，需要手动复制到SageMath中运行
    """
    assert is_sage(), ImportError(f"Error: the function [{inspect.currentframe().f_code.co_name}] is need to run on SageMath.")
    from .Util.sage.RSA.extended_wiener_attack_v3 import _attack

    raise EnvironmentError("please check the path to the code and copy it to SageMath and run it")

def boneh_durfee_attack(e1, e2, e3, n):
    """
    Boneh Burfee攻击
    Sage脚本，无法import使用，需要手动复制到SageMath中运行
    """
    assert is_sage(), ImportError(f"Error: the function [{inspect.currentframe().f_code.co_name}] is need to run on SageMath.")
    from .Util.sage.RSA.boneh_durfee import _attack

    raise EnvironmentError("please check the path to the code and copy it to SageMath and run it")