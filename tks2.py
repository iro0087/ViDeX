from openpyxl import load_workbook

import os, fitz, io, sys

from PIL import Image

from termcolor import colored

from console_progressbar import ProgressBar

filename_ = str(input("What is the folder containing the pdf to convert? (output=out.mp4)"))

output = "/" + filename_

location = filename_ + "/edit.pdf"

file = location

pdf_file = fitz.open(file)

if os.path.exists(location):

    pb = ProgressBar(total=len(pdf_file),prefix='Here', suffix='Now', decimals=3, length=50, fill='#', zfill='-')

    for page_index in range(len(pdf_file)):
    
        pb.print_progress_bar(page_index)
    
        page = pdf_file[page_index]
        
        image_list = page.get_images()
        
        for image_index, img in enumerate(image_list, start=1):
        
            xref = img[0]
            
            base_image = pdf_file.extract_image(xref)
            
            image_bytes = base_image["image"]
            
            image_ext = base_image["ext"]
            
            image = Image.open(io.BytesIO(image_bytes))
            
            image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))

else:

    print("The folder or the pdf does not exist")

command = "ffmpeg -framerate 30 -pattern_type glob -i '*.jpeg' \
  -c:v libx264 -pix_fmt yuv420p out.mp4"

os.system(command)

command = "rm *.jpeg"

os.system(command)

print("")

print("The video is", colored("out.mp4", "red"))






