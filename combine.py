from PIL import Image
import glob

def get_concat_h_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
    if im1.height == im2.height:
        _im1 = im1
        _im2 = im2
    elif (((im1.height > im2.height) and resize_big_image) or
          ((im1.height < im2.height) and not resize_big_image)):
        _im1 = im1.resize((int(im1.width * im2.height / im1.height), im2.height), resample=resample)
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize((int(im2.width * im1.height / im2.height), im1.height), resample=resample)
    dst = Image.new('RGB', (_im1.width + _im2.width, _im1.height))
    dst.paste(_im1, (0, 0))
    dst.paste(_im2, (_im1.width, 0))
    return dst

leftpics=glob.glob("left/*")
rightpics=glob.glob("right/*")
num2combine=len(leftpics)
if (len(leftpics) != len(rightpics)):
 print("Warning! Left and right number of pictures do not match!")
 num2combine=min(len(rightpics),len(leftpics))

for i in range(0,num2combine):
 im1 = Image.open(leftpics[i])
 im2 = Image.open(rightpics[i])
 name='output/combined'+str(i+1)+'.jpg'
 #print(name)
 get_concat_h_resize(im1, im2).save(name)

print('finished')
