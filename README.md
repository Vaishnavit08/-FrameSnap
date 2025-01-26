# Video to Frames Converter

This project extracts frames from a video and saves them as individual image files in a specified folder. It allows you to process videos frame by frame and store them for further analysis or use.

## Features
- Breaks a video into multiple frames.
- Saves frames as image files in a specified folder.
- Allows you to customize the naming pattern of the frames.
- Displays each frame while processing.

## Prerequisites
Ensure you have the following installed:

- Python 3.6 or later
- OpenCV library (`cv2`)

Install the required library using pip:
```bash
pip install opencv-python
```

## How to Use
1. Place your video file (e.g., `nature.mp4`) in the same directory as the script or specify the full path to the video file.
2. Update the folder path in the script where the frames will be saved. For example:
   ```python
   r'C:\Users\Vaishnavi\OneDrive\Desktop\pr\cv\frames\'
   ```
3. Run the script using Python:
   ```bash
   python video_to_frames.py
   ```
4. Each frame will be saved as an image with names like `imgN0.jpg`, `imgN1.jpg`, etc., in the specified folder.
5. Press the `v` key to stop the process at any time.

## Code Explanation

### Imports
- `cv2`: Used for video processing and handling image files.

### Key Steps
- **Video Capture**: The video is opened using `cv2.VideoCapture`.
- **Frame Extraction**: Frames are read and written to the specified folder using `cv2.imwrite`.
- **Dynamic Frame Display**: Each frame is displayed in a window named `res` while the script runs.
- **Controlled Exit**: The program stops when the `v` key is pressed, releasing resources and closing the display window.


## Notes
- Ensure the folder path exists before running the script, or the script will fail to save the images.
- Adjust the `cv2.CAP_PROP_POS_MSEC` value to control the interval between extracted frames (e.g., 100 ms in this script).
- The video file format should be supported by OpenCV.

## Future Improvements
- Add support for extracting frames from a specific time range.
- Allow user input to specify the frame interval dynamically.
- Include an option to resize frames before saving.



## License
This project is licensed under the MIT License. Feel free to use and modify the code.

---

### Author
[Vaishnavi Pravin Talekar](https://github.com/Vaishnavit08)

Check out more of my projects on [GitHub](https://github.com/Vaishnavit08)!
