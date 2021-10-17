# fit-images-to
Simple script for downscale images to specific width or height.
Main purpose is handling a batch of images. 
I am using it when I need downscale images without editor on my hand.

# Installing
```
git clone https://github.com/Jakeroid/fit-images-to
cd fit-images-to
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Examples of usage

1. Downscale all images to height 200px from ./input directory and save them inside ./output directory.

```
python main.py height 200 ./input ./output
```

2. Downscale all images to width 350px from /home/user1/Downloads and save them inside /home/user1/Images.

```
python main.py width 350 /home/user1/Downloads /home/user1/Images
```