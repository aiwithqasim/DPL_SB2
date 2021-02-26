import time,timeit,os,sys  
from hashlib import sha512

class Duplython:
    def __init__(self):
        self.home_dir = os.getcwd(); self.File_hashes = []
        self.Cleaned_dirs = []; self.Total_bytes_saved = 0
        self.block_size = 1024; self.count_cleaned = 0    #Setting Block size to 1kB

    def welcome(self)->None:
        print('******************************************************************')
        print('****************        DUP-SB2        ***************************')
        print('******************************************************************\n\n')
        print('-------A New Way of Deleting Duplicate Files through Python-------')
        time.sleep(5)
        print('\n....Cleaning in Progress \n....Please Wait!')

    def generate_hash(self, Filename:str)->str:
        Filehash = sha512()
        try:
            with open(Filename, 'rb') as File:
                fileblock = File.read(self.block_size)
                while len(fileblock)>0:
                    Filehash.update(fileblock)
                    fileblock = File.read(self.block_size)
                Filehash = Filehash.hexdigest()
            return Filehash
        except:
            return False

    def clean(self)->None:
        all_dirs = [path[0] for path in os.walk('.')]         
        for path in all_dirs:
            os.chdir(path)
            All_Files =[file for file in os.listdir() if os.path.isfile(file)]
            for file in All_Files:
                filehash = self.generate_hash(file)
                if not filehash in self.File_hashes:
                    if filehash:                       
                        self.File_hashes.append(filehash)
                        print("Scanning.......", os.getcwd())
                else:
                    byte_saved = os.path.getsize(file); self.count_cleaned+=1
                    self.Total_bytes_saved+=byte_saved
                    os.remove(file); filename = file.split('/')[-1]
                    print(f'Found {filename}, ...........Removing')
            os.chdir(self.home_dir)

    def cleaning_summary(self)->None:
        mb_saved = self.Total_bytes_saved/1048576      #Converting Bytes Into Mega Bytes  
        mb_saved = round(mb_saved, 2)                  #Rounding saved space to 2 decimal    
        print('\n\n-----------------FINISHED CLEANING --------------')
        print('****Files cleaned : ', self.count_cleaned)
        print('Total Space saved : ', mb_saved, 'MB')
        print('-------------------------------------------------')
        print('\n\nThankyou for Using this product')

    def main(self)->None:
        self.welcome();self.clean();self.cleaning_summary()
