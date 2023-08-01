from pixilizer import *

if __name__ == "__main__":
    Pix = Pixilizer('en')
    Pix.Description()
    file1 = input('First File Name: ')
    file2 = input('Second File Name: ')
    finalname = input('Final File Name (without .png): ')
    img1 = Pix.pixilize(file1, 1)
    img2 = Pix.pixilize(file2, 0)
    Pix.save(img1,img2,finalname)
