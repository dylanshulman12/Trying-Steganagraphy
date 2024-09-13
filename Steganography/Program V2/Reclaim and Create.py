from PIL import Image
import base64


packageImg1Directory = 'C:/Users/dylan/Downloads/Steganography/Files/base.jpg'
packageImg2Directory = 'C:/Users/dylan/Downloads/Steganography/Files/Tree.jpg'




#Trying to reclaim from img file | 1st half
#------------------------reclaim from 2 images-----------------------------------------------
#grab img 1 and 2's end
with open ('C:/Users/dylan/Downloads/Steganography/afterRun/Img1End.txt', 'r') as img1info: #first img last byte
        endOfFileImg1 = int(img1info.read())
with open ('C:/Users/dylan/Downloads/Steganography/afterRun/Img2End.txt', 'r') as img2info: #second img last byte
        endOfFileImg2 = int(img2info.read())

with open (packageImg1Directory, 'rb') as img1: #img1
     img1.seek(endOfFileImg1) #go to last end (before img data was added)
     foundImgData1 = img1.read() #read that img data and store it
with open (packageImg2Directory, 'rb') as img2: #img2
     img2.seek(endOfFileImg2) #go to last end (before img data was added)
     foundImgData2 = img2.read() #read that img data and store it

#-----------------Delete hidden data from both photos now that we want to recreate the image------------
# with open('C:/Users/dylan/Downloads/Steganography/afterRun/hopeful.txt', 'r') as file:
#     file_data = file.read()

# # Step 2: Search for the string and delete it
# string_to_delete = "b'"
# file_data = file_data.replace(string_to_delete, "")

# # Step 3: Write the modified content back to the file
# with open('C:/Users/dylan/Downloads/Steganography/afterRun/hopeful.txt', 'w') as file:
#     file.write(file_data)



#----------------------------re-put into new img-----------------------------------------------------

with open ('C:/Users/dylan/Downloads/Steganography/afterRun/newImg.jpg', 'wb') as newImg:
        # Convert Base64/decrypted back to binary data
        newImg.write(base64.b64decode(foundImgData1) + base64.b64decode(foundImgData2)) 


#-----------------open new File------------------------------


newImg = Image.open('C:/Users/dylan/Downloads/Steganography/afterRun/newImg.jpg')
newImg.show()

























# img = Image.open('C:/Users/dylan/Downloads/Steganography/Files/afterRun/NewFile.jpg')    
# img.show()




