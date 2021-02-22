import time # For Delay 
import os # To Perform Action In OS
from hashlib import sha256 # For Hashing Of File's Data (Secure Hash Algorithm 256)

class Duplython:
    def __init__(self):
        self.home_dir = os.getcwd() # Python method getcwd() returns current working directory of a process 
        self.File_hashes = [] # File Hashes list
        self.Cleaned_dirs = [] # Cleaned Directory List
        self.Total_bytes_saved = 0 # Cleaned Files Size
        self.block_size = 65536 # Chunk/Block Size 
        self.count_cleaned = 0 # No# Of Files Cleaned
        
    def welcome(self)->None: # (->None) It is a type annotation for the welcome method/function that simply states that this function returns "None"
        print('******************************************************************')
        print('****************        DUPLYTHON      ****************************')
        print('********************************************************************\n\n')
        print('----------------        WELCOME        ----------------------------')
        time.sleep(3) # Suspends (Delays) execution for 3 seconds
        print('\nCleaning .................')
        
    def generate_hash(self, Filename:str)->str: # (->str) It is a type annotation for the generate_hash method/function that simply states that this function returns "str"
        Filehash = sha256()
        try:
            with open(Filename, 'rb') as File: # Read File In Binary mode
                fileblock = File.read(self.block_size) # Read Data Of Block Size From File
                while len(fileblock)>0:
                    Filehash.update(fileblock) # Continue hashing of a message by consuming the next chunk of data
                    fileblock = File.read(self.block_size) # Read Next Data Of Block Size From File
                Filehash = Filehash.hexdigest() # Return the printable digest of the message that has been hashed so far
            return Filehash
        except:
            return False
        
    def clean(self)->None: # (->None) It is a type annotation for the welcome method/function that simply states that this function returns "None"
        all_dirs = [path[0] for path in os.walk('.')] # returns Dir Path Eg: 'C:\dir1\dir2\startdir'
        for path in all_dirs: 
            os.chdir(path) # Change the current working directory to path.
            All_Files =[file for file in os.listdir() if os.path.isfile(file)] # (os.path.isfile(file))Return True if path is an existing regular file.
            for file in All_Files:
                filehash = self.generate_hash(file) #Calling Method generate_hash
                if not filehash in self.File_hashes:
                    if filehash:                       
                        self.File_hashes.append(filehash)
                        #print(file)
                else:
                    byte_saved = os.path.getsize(file) 
                    self.count_cleaned+=1
                    self.Total_bytes_saved+=byte_saved
                    os.remove(file)
                    filename = file.split('/')[-1]
                    print(filename, '.. cleaned ')
            os.chdir(self.home_dir)
            
    def cleaning_summary(self)->None:
        mb_saved = self.Total_bytes_saved/1048576
        mb_saved = round(mb_saved, 2)
        print('\n\n--------------FINISHED CLEANING ------------')
        print('File cleaned  : ', self.count_cleaned)
        print('Total Space saved : ', mb_saved, 'MB')
        print('-----------------------------------------------')
        
    def main(self)->None:
        self.welcome();self.clean();self.cleaning_summary()
        
if __name__ == '__main__':
    App = Duplython()
    App.main()
