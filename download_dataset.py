import requests
import zipfile
import os
from tqdm import tqdm

def download_file(url, filename):
    """Download a file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            pbar.update(size)

def main():
    # Create chest_xray directory if it doesn't exist
    if not os.path.exists('chest_xray'):
        os.makedirs('chest_xray')
    
    # Download the dataset
    print("Downloading chest X-ray pneumonia dataset...")
    
    # Note: This is a direct download link - you might need to get the actual URL from Kaggle
    # For now, let's create a sample structure and provide instructions
    
    print("Since direct download requires authentication, please:")
    print("1. Go to: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia")
    print("2. Click 'Download' button")
    print("3. Extract the zip file to this directory")
    print("4. Rename the extracted folder to 'chest_xray'")
    
    # Create a sample structure for testing
    sample_dirs = [
        'chest_xray/train/NORMAL',
        'chest_xray/train/PNEUMONIA',
        'chest_xray/test/NORMAL', 
        'chest_xray/test/PNEUMONIA',
        'chest_xray/val/NORMAL',
        'chest_xray/val/PNEUMONIA'
    ]
    
    for dir_path in sample_dirs:
        os.makedirs(dir_path, exist_ok=True)
    
    print("\nCreated directory structure:")
    for dir_path in sample_dirs:
        print(f"  - {dir_path}")
    
    print("\nPlease add some sample X-ray images to these directories for testing.")

if __name__ == "__main__":
    main() 