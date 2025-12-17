import requests
import time
import os
from tqdm import tqdm 

# 1. Configuration
DOWNLOAD_DIR = 'downloaded_images'
IMG_URLS = [
    f'https://picsum.photos/1000/1000?random={i}' for i in range(1, 21)
] 

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def download_image(url):
    """Downloads a single image synchronously."""
    try:
        img_name = f"image_{url.split('=')[-1]}.jpg"
        img_path = os.path.join(DOWNLOAD_DIR, img_name)
        
        response = requests.get(url, stream=True, timeout=10) 
        
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
        else:
            return False
            
    except Exception as e:
        return False

def main():
    print(f"🐢 Starting SLOW (Sequential) download of {len(IMG_URLS)} images...\n")
    
    start_time = time.time()
    
    # 2. The Slow Loop
    # No ThreadPoolExecutor here. Just a simple for-loop
    # The computer processes one URL, waits, finishes, and then moves to the next
    for url in tqdm(IMG_URLS, unit="img"):
        download_image(url)

    end_time = time.time()
    
    print("\n" + "="*30)
    print(f"Total Time Taken: {end_time - start_time:.2f} seconds")
    print("="*30)

if __name__ == "__main__":
    main()