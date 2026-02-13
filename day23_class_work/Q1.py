import requests
import threading
import time

urls = [
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.rediff.com",
    "https://www.amazon.in"
]

def download_file(url):
    try:
        response = requests.get(url)

        # Extract filename from URL
        filename = url.split("/")[-1] + ".txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")


if __name__ == "__main__":

    # 1️. Sequential Download
    start_time = time.time()

    for url in urls:
        download_file(url)

    sequential_time = time.time() - start_time
    print(f"\nSequential Download Time: {sequential_time:.2f} seconds")

    # 2️. Threading Download
    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()

    # Wait for all threads
    for thread in threads:
        thread.join()

    threading_time = time.time() - start_time
    print(f"\nThreading Download Time: {threading_time:.2f} seconds")
