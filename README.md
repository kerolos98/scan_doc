# Document Scanner

### An interactive document scanner package built in Python using OpenCV

The scanner takes a poorly scanned image, finds the corners of the document, applies the perspective transformation to get a top-down view of the document, sharpens the image, and applies an adaptive color threshold to clean up the image.

On my test dataset of 280 images, the program correctly detected the corners of the document 92.8% of the time.

This project makes use of the transform and imutils modules from pyimagesearch (which can be accessed [here](http://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)). 

### Usage
```
from scan_doc.scan import DocScanner
scanner = DocScanner(OUTPUT_DIR=r"the storage dir" )
scanner.scan(r"image path")
```

