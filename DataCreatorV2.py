"""
DATA CREATOR V2:

Created by: Rodney Pereira (rodders7811)

This program will create data sets for the use of experimental development.  The datasets are printed on screen and a copy saved onto a
.txt file within the same folder.  Its an excellent, lightweight companion should you need to make use of randomly created data. 

"""






""" ======= initialise variables ======= """

menu = None
order = None
varName = None
size = None
dups = None
filename = None
datalist = {}

""" ======== import libraries ======== """

import random

""" ======= Definitions ======== """
def dataSortAsc():
    
    for i in range(numberSets):
                
        dataset = []
                                 
        count = 0
        while count < size:
            
        
            val = random.randint(0,10000)
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              dataset.sort()
              count += 1
            
            datalist[str(varName) +"_"+ str(i+1)] = dataset

    return datalist

def dataSortDec():
    for i in range(numberSets):
                
        dataset = []
                                 
        count = 0
        while count < size:
            
        
            val = random.randint(0,10000)
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              dataset.sort(reverse=True)
              count += 1
            
            datalist[str(varName) +"_"+ str(i+1)] = dataset

    return datalist

  

def integerNumbers():
    
    for i in range(numberSets):
                
        dataset = []
                                 
        count = 0
        while count < size:
            
        
            val = random.randint(0,10000)
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              count += 1
            
            datalist[str(varName) +"_"+ str(i+1)] = dataset
            if order == "A":
              dataset.sort()
            if order == "D":
              dataset.sort(reverse=True)
            

    return datalist       
                    
def decimalNumbers():
    
    for i in range(numberSets):
        dataset = []

        count = 0
        while count < size:
            
            val = random.randint(0,1000)/1000
            
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              count += 1
                      
              
            datalist[str(varName) +"_"+ str(i+1)] = dataset
            if order == "A":
              dataset.sort()
            if order == "D":
              dataset.sort(reverse=True)
    
    return datalist    
 
def upperCase():
    
    for i in range(numberSets):
        dataset = []
        count = 0
        while count < size:
            val = chr(random.randint(65,90))
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              count += 1
            datalist[str(varName) +"_"+ str(i+1)] = dataset
    
    return datalist


def lowerCase():
    for i in range(numberSets):
        dataset = []
        count = 0
        while count < size:
            val = chr(random.randint(97,122))
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              count += 1
            datalist[str(varName) +"_"+ str(i+1)] = dataset
    
    return datalist



def mixedCase():
    for i in range(numberSets):
        dataset = []
        count = 0
        while count < size:
            val = chr(random.randint(97,122))
            if random.randint(0,1) == 1:
              val = val.upper()
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              count += 1
            datalist[str(varName) +"_"+ str(i+1)] = dataset
    
    return datalist

   
def saveData(datalist):
    
    
    
    """ open a txt file to save datasets: """
    
    fileOut = open(filename + ".txt", "a")
    
    print("DATASET(s):")
    fileOut.write("\n")
    fileOut.write("DATASET(s):\n")
    fileOut.write("Created by dataCreatorV2\n")
    fileOut.write("\n")
    fileOut.write("Data Summary:\n")
    fileOut.write("Number of datasets: ")
    fileOut.write(str(len(datalist)))
    fileOut.write("  ")
    fileOut.write("Dataset size: ")
    fileOut.write(str(size))
    fileOut.write("  ")
    fileOut.write("Duplicates: ")
    fileOut.write(str(dups))
    fileOut.write("\n")
    
    for i in range(55):
      
        fileOut.write("-")
    
    fileOut.write("\n")
    
    for key, value in datalist.items():
           
        print(key," = ", value)
        fileOut.write(key)
        fileOut.write(" = ")
        fileOut.write(str(value))
        fileOut.write("\n")
        
    fileOut.write("\n")

    for i in range(55):
      
        fileOut.write("-")
    
    fileOut.write("\n")
    fileOut.write("END of DATASET")
    fileOut.write("\n")
    fileOut.close()
    
    
        
    print("END DATASET")


""" ====== Menu ======= """


print("Dataset Generator")
print("=================")
print("This application will ask you a few short questions and generate a dataset for you based on your answers.\n")
while True:
    print("Choose a dictionary to build from:")
    print("(a) Integer numbers (0-10000)")
    print("(b) Decimal numbers (0-10000, 3dp)")
    print("(c) Upper case letters")
    print("(d) Lower case letters")
    print("(e) Mixed case letters")
    
    menu = input('Enter a-e: ').upper()
    if menu in ['A','B','C','D','E']:
      break
    else:
      print("Invalid input!\n")
print("\n\n")
while True:
  print("Choose an order: ")
  print("(a) Ascending ")
  print("(d) Descending ")
  print("(u) Unordered")
  order = input('Enter a,d or u: ').upper()
  if order in ['A','D','U']:
    break
  else:
    print("Invalid input!\n")
print("\n\n")
varName = input("Enter the variable name you wish to use for your dataset [d]: ")
if varName == '':
  varName = 'd'
print("\n")
while True:
  try:
    size = int(input('Choose a dataset size (1 upwards): '))
    if size < 1:
      print("One upwards!\n\n")
    else:
      break
  except:
    print("Please enter an integer number!\n\n")
print("\n")
while True:
  dups = input('Accept duplicates? (Y/N): ').upper()
  if dups in ['Y','N']:
    break
  else:
    print("Y or N!\n")
numberSets = int(input("How many datasets are needed? (1 upwards): "))
if numberSets == '':
  numberSets = 1
print("\n")

filename = input("Enter file name: ")


""" ==== Menu Options ===== """
 

if menu == 'A':
    integerNumbers()
    
elif menu == 'B':
    decimalNumbers()
 
elif menu == 'C':
    upperCase()
    
elif menu == 'D':
    lowerCase()
  
elif menu == 'E':
    mixedCase()
  
    
else:
    pass
     

# ====== Print the data ======
saveData(datalist)


