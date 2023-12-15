
#Given P is prime
p = 65537

a = 273246787654

# As per Fermat’s Little Theorem,
# a raise to p-1 modulo p is equal to 1, 
# on the condition that p is prime and a is any integer not divisible by p.

if a%p!=0:
    print('Solution: 1')