import random


def is_prime(value) -> bool:
    div = 2
    while value % div != 0:
        div += 1
    return div == value


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_primitive_root(value) -> int:
    roots = []
    required_set = set(num for num in range(1, value) if gcd(num, value) == 1)
    for pg in range(1, value):
        actual_set = set(pow(pg, powers) % value for powers in range(1, value))
        if required_set == actual_set:
            roots.append(pg)
    return random.choice(roots)


minRandom = 100
maxRandom = 1000

print('Generate p and g')
primes = [i for i in range(minRandom, maxRandom) if is_prime(i)]
p = random.choice(primes)
print('p = ', p)
g = find_primitive_root(p)
print('g = ', g)

print('Generate Private Keys...')
privateKeyA = random.randrange(0, 10000)
privateKeyB = random.randrange(0, 10000)

print('Private key a = ', privateKeyA, '\nPrivate key b = ', privateKeyB)

print('Generate Public Keys...')
publicKeyA = g ** privateKeyA % p
publicKeyB = g ** privateKeyB % p
print('Public key A = ', publicKeyA, '\nPublic key B = ', publicKeyB)

secretKeyA = publicKeyB ** privateKeyA % p
secretKeyB = publicKeyA ** privateKeyB % p

print('Secret keys : ', secretKeyA, '=', secretKeyB)


