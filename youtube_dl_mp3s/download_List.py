import os
import time
import random

LIST_FILE = "list.txt"
ERROR_FILE = "error_links.txt"

def is_youtube_url(url):
    return url and ("youtube.com" in url or "youtu.be" in url)

# Read URLs
urls = []
if os.path.exists(LIST_FILE):
    with open(LIST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            url = line.strip()
            if is_youtube_url(url):
                urls.append(url)
else:
    print(f"Error: {LIST_FILE} not found!")
    input("Press Enter to exit...")
    exit()

if not urls:
    print("No valid YouTube links found!")
    input("Press Enter to exit...")
    exit()

print(f'Found {len(urls)} link(s). Starting download...\n')

failed = []   # Will store failed links

for i, URL in enumerate(urls, 1):
    print(f'[{i}/{len(urls)}] Downloading: {URL}')
    
    command = (
        f'yt-dlp -o "%(title)s.%(ext)s" '
        f'-x --audio-format best --embed-thumbnail --add-metadata '
        f'--retries 20 --fragment-retries 20 '
        f'--sleep-interval 10 --max-sleep-interval 25 '
        f'--limit-rate 5M '
        f'--js-runtimes deno '
        f'--remote-components ejs:github '
        f'"{URL}"'
    )
    
    result = os.system(command)
    
    if result != 0:                    # Non-zero = failed
        failed.append(URL)
        print("❌ Download FAILED - Will be saved to error_links.txt")
    else:
        print("✅ Download completed successfully")
    
    print("-" * 80)
    
    # Pause between downloads
    if i < len(urls):
        wait = random.randint(15, 35)
        print(f"Waiting {wait} seconds before next download...")
        time.sleep(wait)

# ==================== Save Failed Links ====================
if failed:
    with open(ERROR_FILE, "w", encoding="utf-8") as f:
        for url in failed:
            f.write(url + "\n")
    print(f"\n⚠️  {len(failed)} link(s) failed and were saved to {ERROR_FILE}")
else:
    print("\n✅ All downloads completed successfully!")

print("\nFinished!")
input("Press Enter to exit...")