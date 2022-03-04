import binascii
import csv

from Crypto.Util.number import getPrime
import math
from tqdm import tqdm

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

all_primes = []

def ouLaShai(upperBound):
	global all_primes
	filter = {}

	for num in tqdm(range(2,upperBound+1)):
		if(num % 100000 == 0):
			print('\n')
			print(len(all_primes))
		try:
			if filter[str(num)]:
				pass
		except:
			all_primes.append(num)
		for prime in all_primes:
			if num*prime>upperBound:
				break
			filter[str(num*prime)]=True
			if num%prime==0:      #这句是最有意思的地方  下面解释
				break

def to_ascii(h):
	list_s = []
	for i in range(0, len(h), 2):
		list_s.append(chr(int(h[i:i+2], 16)))
	return ''.join(list_s)

if(__name__=="__main__"):
	# string to decimal
	pt = int(open('flag.txt','rb').read().hex(),16)
	print(pt)

	primes = []
	n = 1
	# euler totient
	phi = 1
	# public key
	e = 65537

	while math.log2(n) < 640:
		primes.append(getPrime(32))
		print(getPrime(32))
		n *= (primes[-1])
		phi *= (primes[-1] - 1)

	# No duplicates
	assert(len(primes) == len(list(set(primes))))
	# cipher text
	ct = pow(pt,e,n)

	print("n = " + str(n))
	print("e = 65537")
	print("ct = " + str(ct))

	n = 10588750243470683238253385410274703579658358849388292003988652883382013203466393057371661939626562904071765474423122767301289214711332944602077015274586262780328721640431549232327069314664449442016399
	ct = 2093679529573280822046118784413700108333955356566436078249435745673869110116883084133929754933311199736732547505892559695135678800481469602859356500165748152612256935469597540381698322759986797887837

	# lizi
	#primes.clear()
	#primes.append(137)
	#primes.append(131)
	#primes.append(127)
	#n = 2279269
	#phi = 2227680

	'''
	primes.clear()
	while (n != 0):
		i = getPrime(32)
		print(i)
		if (n % i == 0):
			primes.append(i)
			n /= i
			break
	'''
	# 整那么多没用的 yafu一键搞定 泪目
	'''
	ouLaShai(5000000000)
	print(len(all_primes))

	with open('all_primes.csv', "w", newline='') as f:
		writer = csv.writer(f)
		for i in range(len(all_primes)):
			if (i % 100000 == 0):
				print(i)
			writer.writerow([str(all_primes[i])])

	primes.clear()
	while (n != 0):
		for i in all_primes:
			if(n % i == 0):
				primes.append(i)
				n /= i
				break

	with open('all_primes_rrr.csv', "w", encoding='utf-8', newline='') as f:
		writer = csv.writer(f)
		for i in range(len(primes)):
			writer.writerow(str(primes[i]))
	'''
	primes.clear()
	primes.append(3438516511)
	primes.append(2319991937)
	primes.append(2151055861)
	primes.append(2784469417)
	primes.append(3789550043)
	primes.append(2865965429)
	primes.append(2448497717)
	primes.append(3673658161)
	primes.append(3092165243)
	primes.append(2341310833)
	primes.append(4147385899)
	primes.append(3663803701)
	primes.append(3526137361)
	primes.append(2493514393)
	primes.append(3866428117)
	primes.append(2586983803)
	primes.append(3919632263)
	primes.append(3218701459)
	primes.append(2816940109)
	primes.append(2758321513)
	primes.append(2391906757)

	phi = 1
	for i in range(len(primes)):
		phi *= (primes[i] - 1)
	print("phi = " + str(phi))
	d=pow(e, -1, phi)
	print(d)
	d=modinv(e, phi)
	print(d)

	m = pow(ct, d, n)
	print("m = " + str(m))
	c = pow(m,e,n)
	print("c = " + str(c))
	mj = pow(c,d,n)
	print("mj = " + str(mj))
	print(m == mj)

	'''
	for i in range(80000):
		d = float(i * phi + 1) / float(e)
		# print(d)
		print(i)
		m = pow(ct,int(d),n)
		if(pow(m,e,n)==ct):
			print("yes!")
			break
	'''
	# 密文：561417853915350816396509511987299019759664911801611469302961489113206322560582096367436207914250

	x = hex(m)
	print(x)
	x = to_ascii("43495459467b5253415f31735f494d70726f7633645f74305f4d753174695f7633727369306e7d0a")
	print(x)