from PIL import Image
print("Image导入信息",Image,type(Image))

imgPath = "1.png"

#将字符串类型转换为列表类型
char_list = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")
charPic = ""  #保存像素获取到的字符的

#1、获取图片
def openImg():
    img = Image.open(imgPath)
    img.resize((int(img.size[0]),int(img.size[1])),Image.NEAREST)
    print(img.size)
    return img

#2、获取像素值
def getPixel(img):
    global charPic
    print(img.size)
    for y in range(0,img.size[1]):
        for x in range(0,img.size[0]):
            pixel = img.getpixel((x,y))
            charPic += countGray(*pixel)
        charPic+="\n"


#3、计算灰色素
def countGray(r,g,b,a=256):
    if a == 0:
        return " "
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    char = char_list[int(gray/(256/len(char_list)))]
    return char

#4、保存
def saveTxt():
    file = open("转换的字符画.txt","w",encoding="utf-8")
    file.write(charPic)
    file.flush()
    file.close()
    print("转换成功")

getPixel(openImg())
saveTxt()