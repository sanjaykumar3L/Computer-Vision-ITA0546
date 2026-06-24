import cv2

logo = cv2.imread("C:/Users/lsk87/OneDrive/Desktop/Green-Lantern.png")
img = cv2.imread("C:/Users/lsk87/OneDrive/Desktop/download (1).jpg")

h_logo, w_logo = logo.shape[:2]
h_img, w_img = img.shape[:2]

if h_logo > h_img or w_logo > w_img:
    logo = cv2.resize(logo, (w_img // 4, h_img // 4))
    h_logo, w_logo = logo.shape[:2]

center_y = h_img // 2
center_x = w_img // 2

top_y = center_y - h_logo // 2
left_x = center_x - w_logo // 2

destination = img[top_y:top_y + h_logo, left_x:left_x + w_logo]

result = cv2.addWeighted(destination, 1, logo, 0.5, 0)

img[top_y:top_y + h_logo, left_x:left_x + w_logo] = result

cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
