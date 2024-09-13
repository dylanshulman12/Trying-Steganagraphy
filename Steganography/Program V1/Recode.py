from PIL import Image
import base64

#recoding and creating a new image 



#Reopen txt and recode
with open ('C:/Users/dylan/Downloads/Steganography/Files/afterRun/firstHalf.txt', 'r') as file1Str:
        # Convert Base64 back to binary data
        binaryFirstContent = base64.b64decode(file1Str.read())


with open ('C:/Users/dylan/Downloads/Steganography/Files/afterRun/secondHalf.txt', 'r') as file2Str:
        # Convert Base64 back to binary data
        binarySecondContent = base64.b64decode(file2Str.read())


#Create a new image
with open('C:/Users/dylan/Downloads/Steganography/Files/afterRun/NewFile.jpg', 'wb') as n:
    n.write(binaryFirstContent + binarySecondContent)



img = Image.open('C:/Users/dylan/Downloads/Steganography/Files/afterRun/NewFile.jpg')    
img.show()




#First open file, and get size, then split in half save both haves to variable
#decode out of binary
#open file 1 and 2(not file im hiding) then store 2 halves in the end of those files
#delete file, write the name in a new txt file called index
