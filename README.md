# ViDeX

Works ewclusively on GNU/Linux.

Requirement: python librairies

                      - cv2, os, shutil, termcolor, console_progressbar, openpyxl, PIL, fitz, io
                      
             packages
             
                     - texlive (LaTeX)
                     
                     -ffmpeg
                     
                     

"tks.py" converts a video to pdf and create a tex file with the frames of the video in the background.

You can also choose a new framerate for the video to have a faster "pdflatex -halt-on-error edit.tex" compilation.

Maybe that your compiled pdf will show about a quarter of each frame in the background, so make sure to compile twice. 

![videx_008](https://user-images.githubusercontent.com/114911243/218344211-24930beb-6f4d-45f8-8e66-0ad58dd9ff88.jpg)

"tks2.py" allow to convert the pdf output to a video.

![videx_010](https://user-images.githubusercontent.com/114911243/218483713-727e48bc-1cdf-45f6-9635-95dd32196f09.jpg)

