# fit-images-to
The simple script is for downscaling images to specific widths or heights.
I use it when I need downscale images without an editor in my hand. The primary purpose is to handle a batch of photos.

If you need some assistance or similar software, I could help. Contact me on [LinkedIn](https://www.linkedin.com/in/ivan-karabadzhak-42712113b/) or [Upwork](https://www.upwork.com/freelancers/ivank6).

# Installing
```
git clone https://github.com/Jakeroid/fit-images-to
cd fit-images-to
python -m venv ./venv
source ./venv/bin/activate # (if you use fish shell then use: . ./venv/bin/activate.fish)
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
