import os
import sys
from PIL import Image


#find . -regex .*jpg | xargs python2.7 <file>.py
def resize(img, box, fit, out):
    '''
    @param img: Image -  an Image-object
    @param box: tuple(x, y) - the bounding box of the result image
    @param fix: boolean - crop the image to fill the box
    @param out: file-like-object - save the image into the output stream
    '''
    # Preresize image with factor 2, 4, 8 and fast algorithm
    factor = 1
    while img.size[0]/factor > 2*box[0] and img.size[1]*2/factor > 2*box[1]:
        factor *=2
    if factor > 1:
        img.thumbnail((img.size[0]/factor, img.size[1]/factor), Image.NEAREST)

    # Calculate the cropping box and get the cropped part
    if fit:
        x1 = y1 = 0
        x2, y2 = img.size
        wRatio = 1.0 * x2/box[0]
        hRatio = 1.0 * y2/box[1]
        if hRatio > wRatio:
            y1 = int(y2/2-box[1]*wRatio/2)
            y2 = int(y2/2+box[1]*wRatio/2)
        else:
            x1 = int(x2/2-box[0]*hRatio/2)
            x2 = int(x2/2+box[0]*hRatio/2)
        img = img.crop((x1,y1,x2,y2))

    # Resize the image with best quality algorithm ANTI-ALIAS
    img.thumbnail(box, Image.ANTIALIAS)

    # Save it into a file-like object
    img.save(out, "PNG", quality=95)

if __name__ == '__main__':
    realPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    photoPath = "/Resources/Texture/Photos/"
    for filename in sys.argv[1:]:
        print filename
        realName = filename.split(".")[0].split("/")[-1]+".png"
        img = Image.open(filename)
        out = file(realPath+photoPath+realName, "w")
        resize(img, (300, 300), True, out)
        try:
            img.save(out, "PNG")
        finally:
            out.close()