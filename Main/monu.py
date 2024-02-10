from datetime import datetime
import numpy as np
#from scipy.sparse import csr_matrix
'''------------------------------------------------------------------------------------------------'''

# Generate a random sparse matrix with 1s and 0s
sparse_matrix = np.random.choice([0, 1], size=(10, 300))#10 merchant , 300 pin position

print("Sparse Matrix:")
print(sparse_matrix)
merchant= [771000001,771000002,771000003,771000004,771000005,771000006,771000007,771000008,771000009,771000010]
merchantint= 771000003 # set it to a constant value ,.. can be modified later
mjump=merchantint-771000000  # for searching..
fmerchant=sparse_matrix[mjump-1] # FOR FINAL SEARCHING

'''---------------------------------------------------------------------------------------------'''
array = [18, 19, 12, 16, 20, 19, 17, 12, 15, 17, 13, 15, 16, 19, 12]
# Initialize start of pincode for the first area
start_pincode = 110000

def generate_pincodes(start, count):
    return [start + i for i in range(1, count + 1)]

def generate_all_pincodes(array):
    start_pincode = 110000
    all_pincodes = []
    for number in array:
        pincodes = generate_pincodes(start_pincode, number)
        all_pincodes.extend(pincodes)
        start_pincode += 10000
    return all_pincodes


allpins=generate_all_pincodes(array)
'''--------------------------------------------------------------------------------------'''

# record current timestamp
start = datetime.now()
'''---------------------'''
pin=int(input("enter pin:")) #since users will already enter their pin at start

# we have to know its location in  the all_pincodes
k=int(str(pin)[:2])
jp1=0
jp=k-11 # start pin is 11
for i in  range(jp):
    jp1=jp1+array[i]

base=k*10000

jp2=pin-base

jump=jp1+jp2-1
#check

print('pinfind:',allpins[jump])


'''----------------------------------------------------------------------------'''








# Output the result
print(f'your item : {merchantint} and pin:{allpins[jump]}')
if fmerchant[jump]==1:
    print("your item is deliverable")
else:
    print("not deliverable")






'''--------------------------'''
# record loop end timestamp
end = datetime.now()
# record loop end timestamp
end = datetime.now()

# find difference loop start and end time and display
td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is : {td:.03f}ms")
