from PIL import Image,ImageFilter,ImageOps
img=Image.open('d:\\picture\\1.png')
def dodge(a,b.alpha):
    return min(int(a*225/(256-b*alpha)),255)
def draw(img,blur=25,alpha=1.0):
    img1=img.convert('L')#图片转灰色
    img2=img1.copy()
    img2=ImageOps.invert(img2)
    for i in range(blur):
        img2=img2.filter(ImageFilter.BLUR)
    width,height=img1.size
    for x in range(width):
        for y in range(height):
            a=img1.getpixel((x,y))
            b=img2.getpixel((x,y))
            img1.putpixel((x,y),dodge(a,b,alpha))
        img1.show()
        img1.save('d:\\picture\\2.png')
draw(img)
