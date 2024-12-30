# Image-Sketcher

A simple Python script to transform an image into a pencil sketch using OpenCV. This project demonstrates image processing techniques, making it a great introduction to computer vision.

---

## Repository Details
- **GitHub Profile**: [Shubham Parida](https://github.com/shubham-parida01)
- **Repository Name**: [Image-Sketcher](https://github.com/shubham-parida01/Image-Sketcher)

---

## Features
- Converts any image to a grayscale pencil sketch.
- Utilizes OpenCV's image processing functions for high-quality results.
- Simple and customizable code for learning and experimentation.

---

## How It Works
1. **Image Loading**: Reads the input image using OpenCV's `cv2.imread()`.
2. **Grayscale Conversion**: Converts the original image to grayscale.
3. **Inversion**: Inverts the grayscale image to create a negative effect.
4. **Gaussian Blur**: Applies a blur to the inverted image for smoothing.
5. **Sketch Effect**: Combines the grayscale and inverted blurred images to generate the pencil sketch using division.
6. **Display Results**: Shows both the original and the sketch images side-by-side.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shubham-parida01/Image-Sketcher.git
   cd Image-Sketcher
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python
   ```
3. Place an image file named `example2.jpg` in the project directory or update the script with your image path.

---

## Usage
Run the script:
```bash
python image.py
```

### Output:
- **Original Image**: Displays the input image.
- **Sketch Image**: Displays the pencil sketch version of the input image.

Press any key to close the displayed windows.

---

## Customization
- **Change Image**: Replace `example2.jpg` with the desired image file path.
- **Adjust Blur Effect**: Modify the kernel size in `cv2.GaussianBlur()` for different sketch effects:
  ```python
  blurred = cv2.GaussianBlur(image_invert, (21, 21), 0)
  ```
  - Increase values for a softer sketch.
  - Decrease values for a sharper sketch.
- **Save Sketch**: Add this line to save the generated sketch:
  ```python
  cv2.imwrite("sketch_output.jpg", pencil)
  ```

---

## Example Output
Original Image (`example2.jpg`):
![Original Image Placeholder](/images/original.jpg)

Generated Pencil Sketch:
![Sketch Image Placeholder](/images/output.jpg)

---

## Troubleshooting
- **Image Not Found**: Ensure the image file exists in the project directory and the filename matches.
- **No Display**: Check OpenCV installation and GUI support for your environment.

---

## Contributing
Contributions are welcome! Feel free to open issues or create pull requests to improve this project.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Author
**Shubham Parida**  
GitHub: [@shubham-parida01](https://github.com/shubham-parida01)  
Project Repository: [Image-Sketcher](https://github.com/shubham-parida01/Image-Sketcher)
