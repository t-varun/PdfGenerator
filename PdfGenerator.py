from os import listdir
from fpdf import FPDF
 
path = "D:/Python/Pdf/" # get the path of images
 
imagelist = listdir(path) # get list of all images
imagelist.sort()
 
pdf = FPDF('P','mm','A4') # create an A4-size pdf document 
 
x = 0
y = 0
w = 210
h = 297
 
for image in imagelist:
    pdf.add_page()
    pdf.image(path+image,x,y,w,h)
 
pdf.output("Output_pdf.pdf","F")
