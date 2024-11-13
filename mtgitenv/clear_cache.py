import os
import shutil

def clear_cache(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        if '__pycache__' in dirnames:
            cache_dir = os.path.join(dirpath, '__pycache__')
            print(f'Removing cache directory: {cache_dir}')
            shutil.rmtree(cache_dir)

if __name__ == "__main__":
    project_directory = os.getcwd()  # Get the current working directory
    clear_cache(project_directory)