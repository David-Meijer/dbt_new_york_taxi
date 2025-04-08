import os
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, 'raw_files\\files_to_download.txt')
output_path = os.path.join(script_dir, 'raw_files\\')

def download_data():
    with open(input_file_path, 'r') as file:
        urls = file.readlines()
    for url in urls:
        url = url.strip()
        response = requests.get(url.strip(), stream=True)
        response.raise_for_status()
        filename = os.path.join(output_path, url.split('/')[-1])
        with open(filename, 'wb') as file:
            print ('downloading ' + url + ' ...')
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

download_data()