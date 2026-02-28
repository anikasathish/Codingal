import cv2
import matplotlib.pyplot as plt
image_path = ('cute-dogs-pomeranian-1165744963.jpg')
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape
rect1_width, rect1_height = 150, 150

top_left1 = (20, 20)

bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)
rect2_width, rect2_height = 200,150

top_left2 = (width - rect2_width - 20, height - rect2_height - 20)
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)


center1_x = (top_left1[0] + bottom_right1[0]) // 2
center1_y = (top_left1[1] + bottom_right1[1]) // 2
center2_x = (top_left2[0] + bottom_right2[0]) // 2
center2_y = (top_left2[1] + bottom_right2[1]) // 2

cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 255, 0), -1)
cv2.circle(image_rgb, (center2_x, center2_y), 15, (0, 255, 0), -1)

cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (255, 0, 0), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[1] - 10), font, 0.7, (255, 255, 255), 1)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 255, 255), 1)

cv2.putText(image_rgb, f'Center 1: ({center1_x}, {center1_y})', (10, height - 40), font, 0.6, (255, 255, 255), 1)
cv2.putText(image_rgb, f'Center 2: ({center2_x}, {center2_y})', (10, height - 20), font, 0.6, (255, 255, 255), 1)
arrow_start = (center1_x, center1_y)
arrow_end = (center2_x, center2_y)
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 0, 0), 2, tipLength=0.1)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 0, 0), 2, tipLength=0.1)
height_label_position = (arrow_start[0] + (arrow_end[0] - arrow_start[0]) // 2, arrow_start[1] - 10)
cv2.putText(image_rgb, 'Height', height_label_position, font, 0.6, (255, 255, 255), 1)
plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.axis('off')
plt.show()






