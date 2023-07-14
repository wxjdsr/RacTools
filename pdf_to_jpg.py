import os
from pdf2image import convert_from_path

def pdf_to_jpg(pdf_path, page_number, output_folder):
    images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f'page_{page_number}.jpg'), 'JPEG')
        break  # Uncomment this line if you only want to convert the first page

# Usage example
pdf_path = input("Please enter your input file pdf path: ")  # Replace with your PDF file path
page_number = input("Please Enter the page to convert: ")  # Replace with the page number you want to convert (1-based index)
output_folder = input("Please enter the output jpg file path: ")  # Replace with the desired output folder path

pdf_to_jpg(pdf_path, page_number, output_folder)
