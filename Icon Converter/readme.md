This code converts other image formats to the .ico format.

<h3>Create_Icon.py</h3>
Can be imported into other scripts.
Contains a single function that takes a path to an image and the path where the image will be saved. It then crops the image (if not square), resizes it, and saves it as the provided output. To generate a .ico file, you must specify the output as "filename.ico".

<h3>Create_Icon_FileDialog.py</h3>
Can be used directly.
This script uses "Create_Icon.py" to convert an image that is selected from a file dialog. This script also opens a second filedialog to select the output directory and name.

<h3>How to verify .ico files</h3>
The created images can be verified by placing them on the desktop and then creating a shortcut that uses the image as its icon.

<h3>Future Improvements</h3>
In another version of this code, I have the program take in the contents of the clipboard as the image. It output the converted image to the downloads folder. I might upload that code at a later date. However, I've been having some issues with other programs that use the same clipboard library. 
