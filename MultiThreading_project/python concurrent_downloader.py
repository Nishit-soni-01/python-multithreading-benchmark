import threading
import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm  

# 1. Configuration
DOWNLOAD_DIR = 'downloaded_images'
IMG_URLS = [
    f'https://picsum.photos/1000/1000?random={i}' for i in range(1, 21)
] 

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def download_image(url):
    """Downloads a single image."""
    try:
        img_name = f"image_{url.split('=')[-1]}.jpg"
        img_path = os.path.join(DOWNLOAD_DIR, img_name)
        
        response = requests.get(url, stream=True, timeout=10) 
        
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return f"✅ Success: {img_name}"
        else:
            return f"❌ Failed: Status {response.status_code}"
            
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def main():
    print(f"Starting download of {len(IMG_URLS)} images...\n")
    
    start_time = time.time()
    
    # Using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=5) as executor:
        # 1. Submit tasks and store the 'future' objects in a list
        futures = [executor.submit(download_image, url) for url in IMG_URLS]
        
        # 2. Wrap as_completed() with tqdm for the progress bar
        # total=len(futures) tells the bar when it will hit 100%
        # unit="img" labels the counter
        for future in tqdm(as_completed(futures), total=len(futures), unit="img"):
            
            # result from the finished thread
            result = future.result()
            
    end_time = time.time()
    
    print("\n" + "="*30)
    print(f"Total Time Taken: {end_time - start_time:.2f} seconds")
    print("="*30)

if __name__ == "__main__":
    main()