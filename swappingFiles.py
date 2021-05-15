import os

# opening file 2 and extra file
with open('s2.txt','r') as secondfile, open('s.txt','a') as file:
      
    # read content from second file
    for line in secondfile:
               
             # copying to extra file
             file.write(line)

#removing contents of file 2 
file = open("s2.txt","w") #open file in write mode
file.close() #remove contents of file

# opening file 1 and file 2
with open('s1.txt','r') as firstfile, open('s.txt','a') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # copying to second file
             secondfile.write(line)

#removing contents of file 1 
file = open("s1.txt","w") #open file in write mode
file.close() #remove contents of file

os.rename("s.txt","s1.txt") #renaming extra file as first file

os.rename("s1.txt","s.txt") #renaming first file as extra file