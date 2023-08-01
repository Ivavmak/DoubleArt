from pixilizer import *

if __name__ == "__main__":
    Pix = Pixilizer('ru')
    Pix.Description()
    file1 = input('Имя первого файла: ')
    file2 = input('Имя второго файла: ')
    finalname = input('Имя финального файла (без .png): ')
    img1 = Pix.pixilize(file1, 1)
    img2 = Pix.pixilize(file2, 0)
    Pix.save(img1,img2,finalname)
