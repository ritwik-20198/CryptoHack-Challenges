from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
while True:
    p = getPrime(100)
    q = getPrime(100)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
        break

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373


from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

p, q = 752708788837165590355094155871, 986369682585281993933185289261
n, phi = p * q, (p - 1) * (q - 1)
e = 3
d = inverse(e, phi)
ct = 39207274348578481322317340648475596807303160111338236677373 # from output.txt
print(long_to_bytes(pow(ct, d, n)))