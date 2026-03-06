from email.mime import image

import cv2
import numpy as np
def apply_color_filter(image,filter_type):
    """Applies a color filter to the input image based on the specified filter type."""
    filtered_image = image.copy()
    if filter_type == "red_tint":
        # Increase the red channel intensity
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "green_tint":
        # Increase the green channel intensity
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 50)
    elif filter_type == "blue_tint":
        # Increase the blue channel intensity
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 50)
    elif filter_type == "grayscale":
        # Convert the image to grayscale
        filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
    elif filter_type == "sepia":
        # Apply a sepia filter
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        filtered_image = cv2.transform(filtered_image, kernel)
    else:
        raise ValueError("Unsupported filter type. Please choose from 'red_tint', 'green_tint', 'blue_tint', 'grayscale', or 'sepia'.")
    return filtered_image
image_path = "cute-dogs-pomeranian-116574963.jpg"  
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found.")
else:
    filter_type = "original"

    print("press the following keys to apply filters:")
    print("r - Apply red tint")
    print("g - Apply green tint")
    print("b - Apply blue tint")
    print("i - Increase red intensity")
    print("d - Decrease blue intensity")
    print("q - Quit the program")

    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('i'):
            filter_type = "red_tint"
        elif key == ord('d'):
            filter_type = "blue_tint"
        elif key == ord('q'):
            break
        else:
            print("Invalid key. Please press 'r', 'g', 'b', 'i', 'd', or 'q'.")
            
    cv2.destroyAllWindows()
