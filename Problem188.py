"""
The hyperexponentiation of a number
"""

def pow_mod_recursive(a, x, mod):
    if x == 0 or x == 1:
        return a ** x % mod
    elif x % 2 == 0:
        return pow_mod_recursive(a, x//2, mod) ** 2 % mod
    else:
        return a* pow_mod_recursive(a, x//2, mod)** 2 % mod
    

def pow_mod(a, x, mod):
    pow_value = 1
    while x > 0:
        if x & 1 == 1:
            pow_value = pow_value *a % mod
        a = a ** 2 % mod
        x >>= 1
    return pow_value

if __name__ == '__main__':
    result = 1
    for i in range(1855):
        result = pow_mod(1777, result, 100**8)
    print(result)