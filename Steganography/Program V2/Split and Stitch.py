import os
from PIL import Image
import base64


entries = os.listdir()
print(entries)


# with open('data.txt', 'w') as f:
#     data = 'some data to be written to the file'
#     f.write(data)



imgToHide = 'C:/Users/dylan/Downloads/Steganography/Files/invincible.jpg'

#--------------------------------------split img into 2 parts-------------------------------------
with open(imgToHide, 'rb') as scan:
    
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
    halfHiddenImgContent1 = base64.b64encode(binaryFirstContent).decode('utf-8')
    halfHiddenImgContent2 = base64.b64encode(binarySecondContent).decode('utf-8')
    #print if I wanted to
    # print("Base64 Encoded Second Content:")
    # print(base64SecondContent)
    #save decoded into text files

    # with open ('C:/Users/dylan/Downloads/Steganography/afterRun/firstHalf.txt', 'w') as file1Str:
    #     file1Str.write(base64FirstContent)

    # with open ('C:/Users/dylan/Downloads/Steganography/afterRun/secondHalf.txt', 'w') as file2Str:
    #     file2Str.write(base64SecondContent)

#-----------------------------------------------------------------
   
  


# ------------------- inserting image into hidden images ----------------------------------
#recoding and creating a new image 
packageImg1Directory = 'C:/Users/dylan/Downloads/Steganography/Files/base.jpg'
packageImg2Directory = 'C:/Users/dylan/Downloads/Steganography/Files/Tree.jpg'

#Open img1 and get bottom of file position
with open (packageImg1Directory, 'rb') as temp:
    temp.seek(0, 2) #0 = where to move pointer in file to, 2 means start counting from end of file
    endOfImg1 = temp.tell()

#img 2
with open (packageImg2Directory, 'rb') as temp:
    temp.seek(0, 2) #0 = where to move pointer in file to, 2 means start counting from end of file
    endOfImg2 = temp.tell()

#save both to their own files for "memory" img1 then img2
with open ('C:/Users/dylan/Downloads/Steganography/afterRun/Img1End.txt', 'w') as img1info: #first img last byte
        img1info.write(str(endOfImg1))
with open ('C:/Users/dylan/Downloads/Steganography/afterRun/Img2End.txt', 'w') as img2info: #second img last byte
        img2info.write(str(endOfImg2))



#stego into both package images

with open (packageImg1Directory, 'a') as file1Str:
        file1Str.write(halfHiddenImgContent1)

with open (packageImg2Directory, 'a') as file2Str:
        file2Str.write(halfHiddenImgContent2)


#delete file that we just hid
os.remove('C:/Users/dylan/Downloads/Steganography/Files/invincible.jpg')


