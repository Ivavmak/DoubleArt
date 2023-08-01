from PIL import Image
from art import tprint


class Pixilizer():
    def __init__(self,lang):
        self.lang = lang

    def Description(self):
        if self.lang == 'ru':
            tprint('DoubleArt','calgphy2')
            print('Создал Ivavman.\n\nЕсли файл не появился проверьте названия файлов и попробуйте ещё раз.\n\nверсия alpha 1.0.0\n')
        else:
            tprint('DoubleArt','calgphy2')
            print('Created by Ivavman.\n\nIf the file is not created, check the file name and try again.\n!!!In file names, except for the last one, you need to specify the format!!!\n\nver alpha 1.0.0\n')

    def pixilize(self, filename, step):
        img = Image.open(filename).convert('RGBA')
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                if (step == 1):
                    if (j + i) % 2 == 0:
                        pixels[i, j] = 0, 0, 0, 0
                if (step == 0):
                    if (j + i) % 2 != 0:
                        pixels[i, j] = 0, 0, 0, 0
        return img

    def save(self, img1, img2, finalname):
        x, y= img1.size
        x1, y1 = img2.size
        if x > x1:
            biggerimg = img1
            smallerimg = img2

            x, y = biggerimg.size
            x1, y1 = smallerimg.size
        else:
            biggerimg = img2
            smalelrimg = img1

            x, y = biggerimg.size
            x1, y1 = smallerimg.size
        biggerimg.paste(smallerimg, (int((x-x1)/2),int((y-y1)/2)), smallerimg)
        biggerimg.save(f'{finalname}.png')
        if self.lang == 'ru':
            print('Выполнено!')
        else:
            print('Finished!')
