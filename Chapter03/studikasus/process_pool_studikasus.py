#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing
from time import ctime, sleep
import random
import time

def test(data):
    result = data*data
    return result

bangunan1 = 'Kos'
bangunan2 = 'Kontrakan'
nama = ['Pack Udien', 'Bu Marinie']

if __name__ == '__main__':
    inputs1 = list(range(9,10))
    inputs2 = list(range(19,20))
    
    pool = multiprocessing.Pool(processes=4)
    pool_outputs1 = pool.map(test, inputs1)
    pool_outputs2 = pool.map(test, inputs2)
    
    pencari1 = bangunan1
    pencari2 = bangunan2
    
    time.sleep(random.randrange(0, 10))
    print (f'Pencarian Tempat Hidup Sementara: \n Jenis Bangunan: %s \n Nomor Bangunan: %s \n Tanggal: %s \n' % (pencari1, pool_outputs1, ctime()))
    print (f'Pencarian Tempat Hidup Sementara: \n Jenis Bangunan: %s \n Nomor Bangunan: %s \n Tanggal: %s \n' % (pencari2, pool_outputs2, ctime()))
    
    pool.close() 
    pool.join()  
    print('Selesai')