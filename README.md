# Image Filtering with Predefined Kernels

## Overview

This Python script applies image filtering operations using predefined kernels on an input image. Here are the key points about the script:

### Functionality

The script applies various image filtering operations such as blur, emboss, and sharpening.

### Kernel Application

It applies kernels to all channels of a colored image, splitting it into red, green, and blue channels, then merging them after filtering.

### Main Components

The script defines functions for applying kernels on single channels and all channels, along with a dictionary of predefined kernels.

### Input and Output

It prompts the user to select an image file and a kernel for filtering, then displays the original image, the filtered image using the selected kernel, and the filtered image using OpenCV's `filter2D` function.

### Dependencies

Requires NumPy, OpenCV (cv2), and Matplotlib libraries for image processing, numerical operations, and visualization.

### Customization

Users can easily extend functionality by adding or modifying kernels in the predefined dictionary.

## Usage

1. **Prerequisites:**

   - Python 3
   - NumPy
   - OpenCV (cv2)
   - Matplotlib

2. **Setup:**

   - Install the required dependencies using pip:
     ```
     pip install numpy opencv-python matplotlib
     ```

3. **Running the Script:**

   - Run the script in your Python environment:
     ```
     python image_filtering.py
     ```

4. **Input:**

   - Enter the filename of the image you want to process when prompted.

5. **Selecting Kernel:**

   - Choose a kernel from the available options presented.

6. **Output:**

   - View the original image, the filtered image using the selected kernel, and the filtered image using OpenCV's `filter2D` function.

## Conclusion

This script offers a simple yet effective way to apply various image filtering operations using different kernels. Feel free to customize and enhance the functionality according to your requirements.
