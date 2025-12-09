import os
import requests
from pathlib import Path

# Create directories if they don't exist
media_services_dir = Path('media/services')
media_store_dir = Path('media/store')

media_services_dir.mkdir(parents=True, exist_ok=True)
media_store_dir.mkdir(parents=True, exist_ok=True)

# Service images mapping
service_images = {
    'birthday_party.jpg': 'https://picsum.photos/500/400?random=1',
    'catering_corporate.jpg': 'https://picsum.photos/500/400?random=2',
    'catering_party.jpg': 'https://picsum.photos/500/400?random=3',
    'catering_wedding.jpg': 'https://picsum.photos/500/400?random=4',
    'corporate_event.jpg': 'https://picsum.photos/500/400?random=5',
    'event_management.jpg': 'https://picsum.photos/500/400?random=6',
    'photography_event.jpg': 'https://picsum.photos/500/400?random=7',
    'photography_portrait.jpg': 'https://picsum.photos/500/400?random=8',
    'photography_wedding.jpg': 'https://picsum.photos/500/400?random=9',
    'printing_banner.jpg': 'https://picsum.photos/500/400?random=10',
    'printing_cards.jpg': 'https://picsum.photos/500/400?random=11',
    'wedding_planning.jpg': 'https://picsum.photos/500/400?random=12',
}

# Store item images
store_images = {
    'decorations_1.jpg': 'https://picsum.photos/500/400?random=13',
    'decorations_2.jpg': 'https://picsum.photos/500/400?random=14',
    'flowers_1.jpg': 'https://picsum.photos/500/400?random=15',
    'flowers_2.jpg': 'https://picsum.photos/500/400?random=16',
    'lights_1.jpg': 'https://picsum.photos/500/400?random=17',
    'lights_2.jpg': 'https://picsum.photos/500/400?random=18',
    'supplies_1.jpg': 'https://picsum.photos/500/400?random=19',
    'supplies_2.jpg': 'https://picsum.photos/500/400?random=20',
}

def download_images(image_dict, directory):
    """Download images from URLs and save them"""
    for filename, url in image_dict.items():
        filepath = directory / filename
        if not filepath.exists():
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    print(f"✓ Downloaded {filename}")
                else:
                    print(f"✗ Failed to download {filename} (HTTP {response.status_code})")
            except Exception as e:
                print(f"✗ Error downloading {filename}: {e}")
        else:
            print(f"⊘ {filename} already exists")

print("Downloading service images...")
download_images(service_images, media_services_dir)

print("\nDownloading store item images...")
download_images(store_images, media_store_dir)

print("\n✓ All images processed!")
