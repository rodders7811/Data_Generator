
# ======= initialise variables =======

menu = None
order = None
varName = None
size = None
dups = None
datalist = {}

# ======== import libraries ========

import random

# ======= Definitions ========

def integerNumbers():
    
    for i in range(numberSets):
                
        dataset = []
                                 
        count = 0
        while count < size:
            
        
            val = random.randint(0,10000)
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              count += 1
            
            datalist[str(varName) + str(i+1)] = dataset

    return datalist       
                    
def decimalNumbers():
    
    for i in range(numberSets):
        dataset = []

        count = 0
        while count < size:
            
            val = random.randint(0,10000000)/1000
            if val not in dataset or dups == 'Y':
              dataset.append(val)
              count += 1
              
            datalist[str(varName) + str(i+1)] = dataset
    
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
            datalist[str(varName) + str(i+1)] = dataset
    
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
            datalist[str(varName) + str(i+1)] = dataset
    
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
            datalist[str(varName) + str(i+1)] = dataset
    
    return datalist






    
def printData(datalist):
    
    print("DATASET(s):")
    for i in datalist:
           
        print(i," = ", datalist[i])
        
        
    print("END DATASET")






















# ====== Menu =======


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
    print("(f) Mixed case words   -In progress-")
    menu = input('Enter a-f: ').upper()
    if menu in ['A','B','C','D','E','F']:
      break
    else:
      print("Invalid input!\n")
print("\n\n")
while True:
  print("Choose an order: ")
  print("(a) Ascending -in progress-")
  print("(d) Descending -in progress-")
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
print("\n\n")
while True:
  try:
    size = int(input('Choose a dataset size (1 upwards): '))
    if size < 1:
      print("One upwards!\n\n")
    else:
      break
  except:
    print("Please enter an integer number!\n\n")
print("\n\n")
while True:
  dups = input('Accept duplicates? (Y/N): ').upper()
  if dups in ['Y','N']:
    break
  else:
    print("Y or N!\n\n")
numberSets = int(input("How many datasets are needed? (1 upwards): "))
if numberSets == '':
  numberSets = 1
print("\n\n")

# ==== Menu Options =====


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
  # #Mixed case words
  # lines = open('words.txt').read().splitlines()
  # count = 0
  # while count < size:
  #   val = random.choice(lines)
  #   if val not in dataset or dups == 'Y':
  #     dataset.append(val)
  #     count += 1
  # #print(dataset)
  # 
    

if order == 'A':
  #print('Ascending')
  dataset.sort()
elif order == 'D':
  #print('Descending')
  dataset.sort(reverse=True)
else:
  #print('Unsorted')
  pass


# ====== Print the data ======
printData(datalist)
