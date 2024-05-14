### This Python script performs image filtering operations using predefined kernels on an input image. Key points about the script:

### Functionality

        ```The script applies various image filtering operations such as blur, edge detection, and sharpening.```

# Kernel Application

        It applies kernels to all channels of a colored image, splitting it into red, green, and blue channels, then merging them after filtering.

# Main Components

        The script defines functions for applying kernels on single channels and all channels, along with a dictionary of predefined kernels.

# Input and Output

        It prompts the user to select an image file and a kernel for filtering, then displays the original image, the filtered image using the selected kernel, and the filtered image using OpenCV's filter2D function.

# Dependencies

        Requires NumPy, OpenCV (cv2), and Matplotlib libraries for image processing, numerical operations, and visualization.

# Customization

        Users can easily extend functionality by adding or modifying kernels in the predefined dictionary.

## Overall, this script provides a simple and effective way to apply various image filtering operations using different kernels.
