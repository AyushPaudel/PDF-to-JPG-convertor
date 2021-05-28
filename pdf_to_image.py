import shutil
import time
import concurrent.futures
from pdf2image import convert_from_path
import os
directory = os.getcwd()
to_save = directory + "/converted"     # saves in pwd/converted
os.mkdir(to_save)
pdf_name = input("Name of the pdf file")
def download_image(args):
    i, img_url = args
    img_url.save(f'{to_save}/page{i}.jpg', 'JPEG')
    print("Saved")

t1 = time.perf_counter()
print("Collecting")
img_urls = convert_from_path(f'{pdf_name}.pdf', output_folder = directory +"/new" )    # if dir "new" exists in pwd, change new to something else
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, enumerate(img_urls))
t2 = time.perf_counter()
print("Time taken",t2 - t1)

shutil.rmtree(directory +"/new" )
