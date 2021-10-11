import argparse
from PIL import Image
from resizeimage import resizeimage
from os import listdir
from os.path import isfile, join


description = 'Script could downscale images to specific width/height.'
usage = '%(prog)s type value input_dir output_dir'
parser = argparse.ArgumentParser(description=description, usage=usage)
parser.add_argument('type', help='could be width or height')
parser.add_argument('value', help='pixels count')
parser.add_argument('input_dir', help='input directory with images')
parser.add_argument('output_dir', help='output directory with images')
args = parser.parse_args()


files = []
for f in listdir(args.input_dir):

    f_path = join(args.input_dir, f)
    if not isfile(f_path):
        continue

    if f[0] == '.':
        continue

    files.append(f)


for f in files:

    print('Processing ' + f + '...')

    input_f = join(args.input_dir, f)
    output_f = join(args.output_dir, f)

    fd_img = open(input_f, 'rb')
    img = Image.open(fd_img)

    target_value = int(args.value)
    if args.type == 'width':
        img = resizeimage.resize_width(img, target_value)
    elif args.type == 'height':
        img = resizeimage.resize_height(img, target_value)

    img.save(output_f, img.format)
    fd_img.close()


print('Finished!')

