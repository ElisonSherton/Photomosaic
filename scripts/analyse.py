import PIL.Image
import numpy as np

# Analyse the RGB components of our Image
def get_image_stats(img_pth):
    # Read in the image
    i = PIL.Image.open(img_pth)

    # Get the individual channels of image and take mean over the channel
    get_component = lambda x: np.array(i)[:, :, x]
    mR, mG, mB = [np.mean(get_component(x)) for x in range(3)]

    # Get the original size i.e. w, h of the image
    W, H = i.size

    return {"meanR": mR,
            "meanG": mG,
            "meanB": mB,
            "width": W,
            "height": H}