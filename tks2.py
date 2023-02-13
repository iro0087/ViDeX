from openpyxl import load_workbook

import os, fitz, io, sys, time

from PIL import Image

from termcolor import colored

from console_progressbar import ProgressBar

filename_ = str(input("What is the folder containing the pdf to convert? (output=out.mp4)"))

output = "/" + filename_

location = filename_ + "/edit.pdf"

file = location

pdf_file = fitz.open(file)

command = "> fileorder.txt"

os.system(command)

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

command = "mkdir jpeg && cp *.jpeg jpeg/ && ls -1v jpeg > fileorder.txt"

os.system(command)

command = "> fileorder2.txt"

with open("fileorder.txt", "r") as file:

    for line in file:

        with open("fileorder2.txt", "a") as file:

            file.write("file '" + line.strip() + "'\n")

command = "ffmpeg -f concat -i fileorder2.txt -crf 20 -vf fps=25,format=yuv420p out.mp4"

os.system(command)

command = "rm -rf jpeg"

os.system(command)

print("")

print("The video output is", colored("out.mp4", "red"))







