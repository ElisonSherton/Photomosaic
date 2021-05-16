import os
import PIL.Image
import numpy as np

def congregate_images(image_array, W = 3000, w = 250, base_path = "../../Photomosaic_Data/Width_based_crop"):
    
    N = W // w

    final_image = np.zeros((W, W, 3))

    for i in range(N):
        for j in range(N):
            x_start, x_end = w * i, w * (i + 1)
            y_start, y_end = w * j, w * (j + 1)

            sub_image_path = os.path.join(base_path, image_array[i][j])
            substitute_img = np.array(PIL.Image.open(sub_image_path))
            final_image[x_start:x_end, y_start:y_end, :] = substitute_img
    
    print(final_image.shape)
    # final_image = PIL.Image.fromarray(final_image.astype(int))

    return final_image



