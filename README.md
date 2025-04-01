# report midterm

Github: https://github.com/Quy3nsss/Image-precessing-mid-report.git

# Bài toán Finding Object detection.

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image.png)

![2.jpg](report%20midterm%201c6460e3ea95801b805ae24e53548aad/2.jpg)

## **Giới thiệu**

Báo cáo này trình bày một phương pháp phát hiện đối tượng sử dụng kỹ thuật template matching trong OpenCV. Thuật toán có khả năng nhận diện nhiều đối tượng đã định nghĩa trước trong một ảnh đích bằng cách so sánh chúng với một tập hợp các ảnh mẫu (template) ở các tỷ lệ khác nhau.

<aside>
💡

- **Ảnh đích**: Một ảnh đã cắt
- **Các template**: các template đối tượng khác nhau
</aside>

- Sử dụng code để cắt các Template ra khỏi ảnh mẫu.

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%201.png)

- Tách ảnh mục tiêu ra.

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%202.png)

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%203.png)

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%204.png)

## **Template Matching**

<aside>
💡

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%205.png)

**Template matching** cho phép chúng ta phát hiện vật thể trong ảnh đầu vào bằng cách sử dụng một ảnh tham chiếu (template) chứa vật thể cần phát hiện. Cách thuật toán hoạt động:

- Trượt ảnh template trên ảnh đầu vào (giống tích chập 2D)
- Ảnh template sẽ được so sánh với cửa sổ trượt tương ứng trên ảnh đầu vào bằng một công thức.

Ưu điểm:

- Nhanh, đơn giản
- Không tốn công làm data

Nhược điểm

- Template phải rất giống với vật thể trong ảnh cả về kích thước độ nghiêng, ... Nếu khác biệt quá lớn sẽ không phát hiện được.
</aside>

## TM_SQDIFF_NORMED + MASK

<aside>
💡

- Sử dụng phương thức TM_SQDIFF_NORMED để đo sự khác biệt bình phương giữa template và ảnh
- kết hợp với mask để loại bỏ background trắng.

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%206.png)

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%207.png)

</aside>

## Tỉ lệ giữa template và object.

<aside>
💡

Template được cắt và đối tượng cần tìm trong ảnh có kích thước khác nhau. Dẫn tới kết quả tìm kiếm đối tượng diễn ra với kết quả không mong muốn. 

![image.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%208.png)

⇒ Giải pháp là Muti scale.

</aside>

## Muti scale: xác định tỉ lệ giữa template và ảnh.

<aside>
💡

**Mutiscale.**

Phương pháp multi-scale. 

- **Tính bất biến với tỷ lệ (Scale Invariance)**: Template matching cơ bản rất nhạy cảm với kích thước, nhưng bằng cách thử template ở nhiều tỷ lệ khác nhau (0.5 đến 1.0), thuật toán có thể phát hiện đối tượng ở các kích thước khác nhau.
- **Độ chính xác cao hơn**: Bằng cách thử 20 tỷ lệ khác nhau, thuật toán có khả năng cao hơn trong việc tìm ra kích thước template phù hợp nhất với đối tượng trong ảnh.
- **Hiệu quả trong việc xử lý đối tượng đa kích thước**: Đặc biệt hữu ích khi không biết trước kích thước chính xác của đối tượng cần tìm trong ảnh đích.
</aside>

## kết quả khi tiền xử lý với **Gray scale**.(Template và Image)

<aside>
💡

Sau khi áp dụng **Gray scale** **+** **Template Matching + Muti scale + mask + TM_SQDIFF_NORMED**

→ ảnh 1 nhận diện được 13/15; ảnh 2: 12/12

</aside>

![Detected Objects_screenshot_30.03.2025.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/Detected_Objects_screenshot_30.03.2025.png)

![res2.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/res2.png)

## kết quả khi tiền xử lý với **Gray scale** **+ Gaussian + Sobel Operator.(**Template và Image**)**

<aside>
💡

Qua thử nghiệm với Gaussian, Median blur ; Candy , Sobel ⇒ nhận thấy được với **Gaussian + Sobel Operator** cho ra kết quả sát và phù hợp hơn.

</aside>

![Gaussian, Median blur ](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%209.png)

Gaussian, Median blur 

![Gaussian blur + Candy or Sobel ](report%20midterm%201c6460e3ea95801b805ae24e53548aad/image%2010.png)

Gaussian blur + Candy or Sobel 

<aside>
💡

Thực hiện xử lý ảnh 1 thêm **Gaussian + Sobel Operator**

- **Làm mờ Gaussian**: Sử dụng bộ lọc Gaussian với kernel `(3,3)` để giảm nhiễu.
- **Phát hiện biên**: Sử dụng **Sobel Operator** để tính gradient theo hai trục X và Y, sau đó kết hợp chúng.

⇒ Đã nhận diện được 15/15 

![Detected Objects_screenshot_01.04.2025.png](report%20midterm%201c6460e3ea95801b805ae24e53548aad/Detected_Objects_screenshot_01.04.2025.png)

</aside>

# Nhận xét chung.

<aside>
💡

Tùy vào ảnh đầu vào mà ta cần chọn phương pháp xử lý phù hợp với phương pháp tìm kiếm mà ta đang sử dụng. 

- Với ảnh 2 chỉ cần xử lý ảnh với Gray scale cho qua Template Matching sử dụng TM_SQDIFF_NORMED + MASK ⇒ Tìm kiếm được 12/12
- Với ảnh 1 xử lý ảnh với Gray scale cho qua Template Matching sử dụng TM_SQDIFF_NORMED + MASK ⇒ Tìm kiếm được 13/15
- Sau khi xử lý thêm với **Gaussian + Sobel Operator** ⇒ Tìm kiếm được 15/15

</aside>