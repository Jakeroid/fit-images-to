from PIL import Image
from resizeimage import resizeimage
from os import listdir
from os.path import isfile, join

input_path = './input'
output_path = './output'

files = [f for f in listdir(input_path) if isfile(join(input_path, f)) and f != '.DS_Store']

for f in files:
    print('Processing ' + f + '...')
    input_f = join(input_path, f)
    output_f = join(output_path, f)
    fd_img = open(input_f, 'rb')
    img = Image.open(fd_img)
    img = resizeimage.resize_width(img, 2250)
    img.save(output_f, img.format)
    fd_img.close()

print('Finished!')

