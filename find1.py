import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('CropImg/cropped_1.jpg')
# convert to Gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_gray = cv2.GaussianBlur(image_gray, (3, 3), 0)

# ret, _ = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# low_threshold = float(ret * 0.5)  
# high_threshold = float(ret)       
# image_gray = cv2.Canny(image_gray, low_threshold, high_threshold)

sobelx = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)

image_gray = np.sqrt(sobelx**2 + sobely**2)

image_gray = np.uint8(255 * image_gray / np.max(image_gray))

templates = [
    "ball", "baloon", "bear", "bow", "boat",
    "bunny", "cake", "car", "duck", "grape",
    "horse", "icecream", "strawberry", "watermelon", "wood"
]

# define the scale factor 
scale_factor = np.linspace(0.5, 1, 20)

for template in templates:
    # load the template image
    template_image = cv2.imread(f'Templates1/{template}.jpg')
    
    # convert template to grayscale
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    
    template_gray = cv2.GaussianBlur(template_gray, (3, 3), 0)
    
    # ret, _ = cv2.threshold(template_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # low_threshold = float(ret * 0.5)  
    # high_threshold = float(ret)       
    # template_gray = cv2.Canny(template_gray, low_threshold, high_threshold)
    
    sobelx = cv2.Sobel(template_gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(template_gray, cv2.CV_64F, 0, 1, ksize=3)
    
    template_gray = np.sqrt(sobelx**2 + sobely**2)
    
    template_gray = np.uint8(255 * template_gray / np.max(template_gray))
    
    # make mask to reject the white background
    _, template_mask = cv2.threshold(template_gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # because TM_SQDIFF_NORMED is used, so the min value is best
    best_val = float('inf')
    best_loc = None
    best_scale = None
    best_template = None
    
    # loop through the scale factor
    for scale in scale_factor:
        # resize the template and mask depending on the scale factor
        new_width = int(template_gray.shape[1] * scale)
        new_height = int(template_gray.shape[0] * scale)
        
        # if template is to small, skip
        if new_width < 10 or new_height < 10:
            continue
        
        template_resized = cv2.resize(template_gray, (new_width, new_height))
        template_mask_resized = cv2.resize(template_mask, (new_width, new_height))
        
        # if template is more than image, skip
        if new_width > image_gray.shape[1] or new_height > image_gray.shape[0]:
            continue
        
        # apply template matching
        result = cv2.matchTemplate(image_gray, template_resized, cv2.TM_SQDIFF_NORMED, mask=template_mask_resized)
        # find the best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # update the best match if found
        if min_val < best_val:
            best_val = min_val
            best_loc = min_loc
            best_scale = scale
            best_template = template_resized
        
    # draw the best match
    if best_loc is not None:
        top_left = best_loc
        bottom_right = (top_left[0] + int(best_template.shape[1] * best_scale), top_left[1] + int(best_template.shape[0] * best_scale))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, f"{template} (scale: {best_scale:.2f})", (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(f"{template}: best scale = {best_scale:.2f}, matching score = {best_val:.3f}")
        
cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()