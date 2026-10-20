#!/usr/bin/env python3
"""
Helper script for your portfolio:
Converts any input photo (PNG, JPG, HEIC, etc.) into all required optimized web formats:
- photo.png  (Lossless original)
- photo.jpeg (True JPEG encoding for cross-browser reliability)
- photo.jpg  (Standard extension copy)
- photo.webp (Modern web format for instant mobile loading)

Usage:
    python3 optimize_photo.py my_picture.jpg
"""

import sys
import os
from PIL import Image

def main():
    if len(sys.argv) < 2:
        # Default to looking for any photo file in current directory
        candidates = ['photo.png', 'photo.jpg', 'photo.jpeg', 'portrait.jpg', 'portrait.png']
        input_path = next((c for c in candidates if os.path.exists(c)), None)
        if not input_path:
            print("Usage: python3 optimize_photo.py <path_to_your_image>")
            sys.exit(1)
    else:
        input_path = sys.argv[1]

    print(f"[*] Processing source image: {input_path}")
    im = Image.open(input_path)
    print(f"[*] Original format: {im.format}, Dimensions: {im.size}, Mode: {im.mode}")

    # Convert to RGB (removing alpha channel for clean JPEG compression)
    rgb_im = im.convert('RGB')

    # Save to all required web formats
    rgb_im.save('photo.jpeg', format='JPEG', quality=95, optimize=True)
    rgb_im.save('photo.jpg', format='JPEG', quality=95, optimize=True)
    rgb_im.save('photo.webp', format='WEBP', quality=95)
    
    # Save lossless PNG
    im.save('photo.png', format='PNG', optimize=True)

    print("[+] Successfully generated:")
    print("    - photo.jpeg (True JPEG, cross-browser verified)")
    print("    - photo.jpg  (JPEG standard)")
    print("    - photo.webp (Optimized WebP for mobile)")
    print("    - photo.png  (Lossless PNG)")
    print("[*] Your portrait is ready to display seamlessly on the website!")

if __name__ == '__main__':
    main()
