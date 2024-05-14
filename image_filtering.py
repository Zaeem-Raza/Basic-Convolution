import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# * Function to Apply kernel on all channels


def Apply_Kernels(img, kernel):
    # 1.colored image has 3 channels --> R, G, B
    # 2.split the image into 3 channels
    # 3.apply the kernel on each channel
    # 4.merge the channels
    R, G, B = cv.split(img)
    red = convolute(R, kernel)
    green = convolute(G, kernel)
    blue = convolute(B, kernel)
    updated = cv.merge((red, green, blue))
    return updated


# * Function to Apply kernel on a single channel

def convolute(image, kernel):
    # store the height and width of the image & kernel
    height, width = image.shape
    kheight, kwidth = kernel.shape
    # applying border to avoid the loss of pixels
    pad_array = np.pad(image, pad_width=(kheight//2, kwidth//2),
                       mode='constant', constant_values=0)
    resultant_image = np.zeros((height, width), dtype=int)

    for i in range(height):
        for j in range(width):
            mat = pad_array[i:i+kheight, j:j+kwidth]

            # ? if the shapes are equal
            if (mat.shape == kernel.shape):
                resultant_image[i, j] = np.sum(mat * kernel)
    return resultant_image


# *   ----> Main <----

#! Define all kernels
kernels = {
    'blur': np.array([0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625]).reshape(3, 3),
    'bottom_sobel': np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1]).reshape(3, 3),
    'emboss': np.array([-2, -1, 0, -1, 1, 1, 0, 1, 2]).reshape(3, 3),
    'identity': np.array([0, 0, 0, 0, 1, 0, 0, 0, 0]).reshape(3, 3),
    'left_sobel': np.array([1, 0, -1, 2, 0, -2, 1, 0, -1]).reshape(3, 3),
    'outline': np.array([-1, -1, -1, -1, 8, -1, -1, -1, -1]).reshape(3, 3),
    'right_sobel': np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1]).reshape(3, 3),
    'sharpen': np.array([0, -1, 0, -1, 5, -1, 0, -1, 0]).reshape(3, 3),
    'top_sobel': np.array([1, 2, 1, 0, 0, 0, -1, -2, -1]).reshape(3, 3)
}

# * Read the image
input_image = input("Enter the image file name: ")
img = cv.imread(input_image)
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# * Prompt user to select a kernel
print("Available kernels:")
for kernel_name in kernels.keys():
    print(kernel_name)
selected_kernel = input("Enter the kernel to apply: ")

# * Apply selected kernel
if selected_kernel in kernels:
    filtered_img = Apply_Kernels(img_rgb, kernels[selected_kernel])
    plt.subplot(1, 3, 1), plt.imshow(img_rgb), plt.title(
        'Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1, 3, 2), plt.imshow(filtered_img), plt.title(
        'Kernel: ' + selected_kernel), plt.xticks([]), plt.yticks([])
    cvfilter = cv.filter2D(img_rgb, -1, kernels[selected_kernel])
    plt.subplot(1, 3, 3), plt.imshow(cvfilter), plt.title(
        'OpenCV filter2D'), plt.xticks([]), plt.yticks([])
    plt.show()
else:
    print("Invalid kernel selected.")
