import shutil
import time
import concurrent.futures
from pdf2image import convert_from_path
import os
import random
import string

directory = os.getcwd()


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return directory + "/" + result_str


pdf_name = input("Name of the pdf file ")
save = input("Save in ")

to_save = directory + "/" + save
try:
    os.mkdir(to_save)
except FileExistsError:
    pass

g = get_random_string(8)
os.mkdir(g)



def download_image(args):
    i, img_url = args
    img_url.save(f'{to_save}/page{i}.jpg', 'JPEG')
    print("Saved")


def main():
    t1 = time.perf_counter()
    print("Collecting")
    img_urls = convert_from_path(f'{pdf_name}.pdf',
                                 output_folder=g)  # if dir "new" exists in pwd, change new to something else
    print(f"Collected {len(img_urls)} pages.")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, enumerate(img_urls))
    t2 = time.perf_counter()
    print("Time taken", t2 - t1)

    shutil.rmtree(g)


if __name__ == "__main__":
    main()
