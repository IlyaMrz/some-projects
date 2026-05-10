import sys
import pyperclip
import subprocess

def get_channel_url():
    try:
        clip = pyperclip.paste().strip()
        if "youtube.com" in clip:
            print(f"Detected in clipboard: {clip[:70]}...")
            if input("Use this link? (y/n): ").lower() == 'y':
                return clip
    except:
        pass
    return input("\nPaste YouTube channel URL: ").strip()


def get_number_of_videos():
    while True:
        try:
            n = int(input("\nHow many latest videos do you want? (1-30): "))
            if 1 <= n <= 30:
                return n
            print("Please enter a number between 1 and 30.")
        except:
            print("Invalid input.")


def get_latest_videos(channel_url, limit=10):
    print("\nFetching latest videos...")

    base = channel_url.rstrip('/')
    if not base.endswith('/videos'):
        videos_url = base + '/videos'
    else:
        videos_url = base

    cmd = [
        'yt-dlp',
        '--flat-playlist',
        f'--playlist-items=1-{limit}',
        '--print', '%(title)s|%(webpage_url)s',
        '--extractor-args', 'youtube:player_client=android,web',
        videos_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=25)

        if result.returncode == 0 and result.stdout.strip():
            videos = []
            for line in result.stdout.strip().split('\n'):
                if line.strip() and '|' in line:
                    title, url = line.split('|', 1)
                    if url.startswith('http'):
                        videos.append((title.strip(), url.strip()))

            if videos:
                print(f"✅ Success! Got {len(videos)} videos.")
                return videos

    except FileNotFoundError:
        print("❌ yt-dlp not found. Run: pip install -U yt-dlp")
        return []
    except Exception as e:
        print(f"Error: {e}")

    print("❌ Failed to fetch videos.")
    return []


def main():
    print("=== YouTube Latest Videos Fetcher ===\n")

    url = get_channel_url()
    limit = get_number_of_videos()

    videos = get_latest_videos(url, limit)

    if not videos:
        return

    # Show nice formatted list with titles
    print(f"\n✅ {len(videos)} Latest Videos:\n")
    for i, (title, link) in enumerate(videos, 1):
        print(f"{i:2d}. {title}")
        print(f"    {link}\n")

    # === Pure links only for clipboard and final output ===
    pure_links = [link for _, link in videos]
    
    try:
        pyperclip.copy("\n".join(pure_links))
        print("✅ All links (clean, one per line) copied to clipboard!")
    except:
        pass

    # Also print clean links in console
    print("\n" + "="*50)
    print("PURE LINKS (one per line):")
    print("="*50)
    for link in pure_links:
        print(link)


if __name__ == "__main__":
    main()