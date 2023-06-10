#Library dan inisialisasi
import random
import math
import matplotlib.pyplot as plt 

ra_x = 5        # batas atas x
rb_x = -5       # batas bawah x
ra_y = 5        # batas atas y
rb_y = -5       # batas bawah y

#Code Program
class chromosome:     
    '''         
    Class untuk menampung kromosom
    '''       
    def __init__(self, biner = None):
        if biner == None:
            self.biner = random.choices([0, 1], k=8)
        else:
            self.biner = biner
        self.x = self.Representation(ra_x, rb_x, self.biner[:4])
        self.y = self.Representation(ra_y, rb_y, self.biner[4:])

    def __repr__(self):
        '''
        Printable representation dari class kromosom
        '''
        return '{} \n Nilai x dan y: ({}, {}) \n Nilai Fitness: {}'.format(self.biner, self.x, self.y, heuristic(self.x, self.y))

    def Representation(self, ra, rb, g):      
        '''   
        Fungsi ini digunakan untuk menghitung nilai representasi 
        Representasi yang digunakan yaitu Representasi biner 1 titik
        '''
        rn = [2**-i for i in range(1, len(g) + 1)]                                      #rentang nilai
        return rb + ((ra - rb) / sum(rn) * sum([g[i] * rn[i] for i in range(len(g))]))  #Rumus representasi biner

def heuristic(x, y):
    '''   
    Fungsi ini digunakan untuk mencari nilai heuristic
    Rumus nilai heuristic yang digunakan dalam fungsi ini didapat dari soal.
    '''
    return (((math.cos(x) + math.sin(y)) ** 2) / ((x**2) + (y**2)))

def fitness(x, y):
    '''
    Fungsi ini digunakan untuk menghitung nilai fitness
    Fungsi fitness yang digunakan adalah maksimum f = h
    '''
    return heuristic(x, y)

def exist(j, l):
    '''
    Fungsi ini digunakan untuk memeriksa jika kromosom ada di populasi dan 
    digunakan juga untuk seleksi orang tua
    '''
    found = False      
    for i in j:
        if i.biner == l.biner:
            found = True
            break
    return found

def parentselection(k):    
    '''
    Fungsi ini digunakan untuk seleksi orangtua 
    Fungsi ini akan mereturn orangtua dari metode Roulette wheel
    '''
    parent = []                                                                       #List atau array orangtua
    list_fitness = list(map(lambda c: fitness(c.x, c.y), populasi))                   #Memakai fungsi lambda sebagai anonymous function
    list_weight = [list_fitness[i] / sum(list_fitness) for i in range(len(populasi))] #List atau array untuk menampung weight dari semua kromosom yang ada di populasi
    while len(parent) != k:
        kandidat = random.choices(populasi, weights=list_weight)[0]                   #Parameter weight akan memberi berat kemungkinan pada setiap nilai
        if not exist(parent, kandidat):                                               #Sehingga setiap item untuk dipilih ditentukan oleh bobot relatifnya.
            parent.append(kandidat)
    return parent

def Crossover(parent1, parent2):        
    '''
    Fungsi crossover digunakan untuk menghasilkan anak
    '''
    pos = random.randint(1, len(parent1.biner) - 2)               #mengambil titik potong dari indeks kedua paling awal atau indek kedua paling akhir, *pos = position

    biner_child1 = parent1.biner[:pos] + parent2.biner[pos:]
    biner_child2 = parent2.biner[:pos] + parent1.biner[pos:]
    '''
    Mutasi
    '''
    #Mutasi anak pertama
    prob_mutasi = random.uniform(0, 100)                          #memilih angka random dari 0 sampai 100 prob_mutasi dalam persen
    if prob_mutasi < 0.5:                                         #0.5% mutasi
        idx_mutasi = random.randint(0, len(biner_child1) - 1)
        if biner_child1[idx_mutasi] == 1:
            biner_child1[idx_mutasi] = 0
        else:
            biner_child1[idx_mutasi] = 1

    #Mutasi anak ke 2
    prob_mutasi = random.uniform(0, 100)                          #Memilih angka random dari 0 sampai 100 prob_mutasi dalam persen
    if prob_mutasi < 0.5:                                         #0.5% mutasi
        idx_mutasi = random.randint(0, len(biner_child2) - 1)
        if biner_child2[idx_mutasi] == 1:
            biner_child2[idx_mutasi] = 0
        else:
            biner_child2[idx_mutasi] = 1

    #Memasukan hasil crossover dan mutasi ke populasi
    populasi.append(chromosome(biner_child1))    
    populasi.append(chromosome(biner_child2))    

def survivorselection(): 
    '''
    Fungsi seleksi survivor berfungsi agar populasi terus sama
    '''
    populasi.sort(key=lambda c: heuristic(c.x, c.y), reverse=True)  #Memakai fungsi key dan fungsi lambda sebagai anonymous function di dalam fungsi sort descending

    while len(populasi) != 100:                                     #Mengatur jumlah populasi agar tetap 100
        populasi.pop()                                              #Membuang kromosom yang paling buruk di populasi 

"""** Program Utama **"""
populasi = []
generasi = 1
while len(populasi) != 100:
    c = chromosome()

    if not exist(populasi, c):
        populasi.append(c)

survivorselection()
print('Generasi', generasi)
print('Best', populasi[0])

arr_fitness = [0]*100
arr_fitness[generasi-1] = fitness(populasi[0].x, populasi[0].y)

while generasi < 100:                                                   #melakukan evolusi sebanyak 100 generasi
    parent = parentselection(2)
    Crossover(parent[0], parent[1])
    survivorselection()

    generasi += 1

    arr_fitness[generasi-1] = fitness(populasi[0].x, populasi[0].y)
    print('Generasi', generasi)
    print('Best Chromosome', populasi[0])  #Output kromosom terbaik dari populasi generasi 'generasi'

#Menampilkan pertumbuhan nilai fitness kromosom terbaik
plt.plot(range(1, generasi + 1), arr_fitness)
plt.title("Pertumbuhan Nilai Fitness")
plt.xlabel("Generasi")
plt.ylabel("Fitness Terbaik")
plt.show()