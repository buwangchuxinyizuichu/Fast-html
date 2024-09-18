import os
import glob


def get_raw_files():
    cwd = os.getcwd()
    raw_files = glob.glob(f'{cwd}/raw/*.psd')
    raw_files = [os.path.basename(file) for file in raw_files]
    return raw_files


def create_directories(file_name):
    base_dir = f'./results/{file_name}/assets'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    files = [
        'images',
        'fonts',
    ]
    for file in files:
        dir_path = os.path.join(base_dir, file)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
