from PIL import Image
import argparse
# # 首先，构建命令行输入参数处理 ArgumentParser 实例
# parser = argparse.ArgumentParser()

# # 定义输入文件、输出文件、输出字符画的宽和高
# parser.add_argument('file')     #输入文件
# parser.add_argument('-o', '--output')   #输出文件
# parser.add_argument('--width', type = int, default = 80) #输出字符画宽
# parser.add_argument('--height', type = int, default = 80) #输出字符画高

# # 解析并获取参数
# args = parser.parse_args()

# # 输入的图片文件路径
# IMG = args.file

# # 输出字符画的宽度
# WIDTH = args.width

# # 输出字符画的高度
# HEIGHT = args.height

# # 输出字符画的路径
# OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    IMG = 'D:\Code\document-uid627425labid1191timestamp1523872533432.png'
    im = Image.open(IMG)
    width=80
    height=80
    im = im.resize((width,height), Image.NEAREST)

    txt = ""

    for i in range(width):
        for j in range(height):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)
