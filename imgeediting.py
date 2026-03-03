from email.mime import image

import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(image, title='cute-dogs-pomeranian-1165744963.jpg'):
    plt.figure(figsize=(8, 6))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(imagepath):
    image = cv2.imread(imagepath)
    if image is None:
        print("Error: Image not found.")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(gray_image, title='Original Grayscale Image')

    print("Select an option:")
    print("1. Canny Edge Detection")
    print("2. Sobel Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothening")
    print("5. Median Filtering ") 
    print("6. Exit") 

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            edges = cv2.Canny(gray_image, 100, 200)
            display_image(edges, title='Canny Edge Detection')
        elif choice == '2':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
            sobel_edges = cv2.magnitude(sobelx, sobely)
            display_image(sobel_edges.astype(np.uint8), title='Sobel Edge Detection')
        elif choice == '3':
            laplacian_edges = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image(laplacian_edges.astype(np.uint8), title='Laplacian Edge Detection')
        elif choice == '4':
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
            display_image(blurred_image, title='Gaussian Smoothening')
        elif choice == '5':
            median_filtered_image = cv2.medianBlur(gray_image, 5)
            display_image(median_filtered_image, title='Median Filtering')
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

interactive_edge_detection('cute-dogs-pomeranian-1165744963.jpg')



