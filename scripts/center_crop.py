import PIL.Image

def center_crop(img, new_w, new_h):
    current_w, current_h = img.size

    # Make sure the new width and new height are smaller than the original image
    # assert current_w > new_w
    # assert current_h > new_h

    # Compute the co-ordinates of the left top and right bottom coordinates
    left = (current_w - new_w) // 2
    right = (new_w + current_w) // 2

    top = (current_h - new_h) // 2
    bottom = (new_h + current_h) // 2
    
    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))

    return cropped_img

