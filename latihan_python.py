#print('aku adalah aku'), print('aku adalah aku')
a=2
b=5
c=4.5
d=('aku adalah aku')
z='12345'
q=True
e, f, g = 5, 6, 7.5

def fungsi1():
    a=1
    b=2
    c=a+b
    return c
#print(fungsi1())

#if a>b: print (a)
#else: print (b)
#print(e, f)
#print(type(c))
#print (d)
#print (d[0:5])
buah={'apel','mangga','jeruk','pepaya','mangga'}
buah2=['apel','mangga','jeruk','pepaya','mangga']
print(buah)
print(buah2)
buah.add ('anggur')


def luas_segitiga(alas,tinggi):
    Luas=1/2* alas * tinggi
    print('luas segitiga adalah: %f' %Luas)
luas_segitiga(4,6)

def persegi_panjang (panjang,lebar):
    Luas=panjang*lebar
    print('Luas persegi panjang adalah %f' %Luas)
persegi_panjang(6,5)



def bilangan_prima(x):
    prima=True
    if x>=2:
        for i in range(2,x):
            if x % i == 0:
                prima=False
    else:
        prima=False
    return prima

for i in range(1,100):
    if bilangan_prima(i):
        print (i)

