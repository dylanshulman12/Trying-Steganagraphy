import os
from PIL import Image
import base64


entries = os.listdir()
print(entries)


# with open('data.txt', 'w') as f:
#     data = 'some data to be written to the file'
#     f.write(data)




with open('C:/Users/dylan/Downloads/Steganography/Files/invincible.jpg', 'rb') as scan:
    
    scan.seek(0, 2) #0 = where to move pointer in file to, 2 means start counting from end of file
    file_size = scan.tell() #get amount of bytes for file at that position(size of file)

    #middle
    middle = file_size//2


    #copying the binary for first and second halfs of files

    #copy first part of file
    scan.seek(0)
    binaryFirstContent = scan.read(file_size//2)

    #copy second part of file
    scan.seek(middle)  # Go back to middle
    binarySecondContent = scan.read(file_size//2)




    #decode binary
    base64FirstContent = base64.b64encode(binaryFirstContent).decode('utf-8')
    base64SecondContent = base64.b64encode(binarySecondContent).decode('utf-8')
   
    #print if I wanted to
    # print("Base64 Encoded Second Content:")
    # print(base64SecondContent)
  

 
#save decoded into text files

    with open ('C:/Users/dylan/Downloads/Steganography/Files/afterRun/firstHalf.txt', 'w') as file1Str:
        file1Str.write(base64FirstContent)

    with open ('C:/Users/dylan/Downloads/Steganography/Files/afterRun/secondHalf.txt', 'w') as file2Str:
        file2Str.write(base64SecondContent)





