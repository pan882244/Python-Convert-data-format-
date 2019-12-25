import os
 
import os

 # 图片输出位置
out_path=r"D:\\aa\\12\\"

def imageDecode(f,fn):
    
    # out='P:\\'+fn+".png"
    # 输出目录是否存在，创建
    if os.path.exists(out_path):
        dat_read = open(f, "rb")
        out=out_path+fn+".png"
        png_write = open(out, "wb")
        for now in dat_read:
            for nowByte in now:
                newByte = nowByte ^ 0x7D # 根据dat文件的文件头与图片的文件头FF D8进行异或计算
                png_write.write(bytes([newByte]))
        dat_read.close()
        png_write.close()
    else :
        os.mkdir(out_path)
        out=out_path+fn+".png"
        png_write = open(out, "wb")
        for now in dat_read:
            for nowByte in now:
                newByte = nowByte ^ 0x7D # 根据dat文件的文件头与图片的文件头FF D8进行异或计算
                png_write.write(bytes([newByte]))
        dat_read.close()
        png_write.close()
 
def findFile(f):
    fsinfo = os.listdir(f)
    for fn in fsinfo:
        temp_path = os.path.join(f, fn)
        if not os.path.isdir(temp_path):
            print('文件路径: {}' .format(temp_path))
            print(fn)
            imageDecode(temp_path,fn)
            
 
path = r'D:\用户目录\我的文档\WeChat Files\wxid_s5aoxxhryecv22\FileStorage\Image\2019-12'
# findFile(path)
 
# path = r'E:\\'
findFile(path)
