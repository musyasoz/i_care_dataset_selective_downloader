# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 2025

@author: neuronauts

I-CARE Dataset Selective Downloader
-----------------------------

This Python script downloads EEG-related files (`_EEG`) from the I-CARE dataset
hosted on PhysioNet, within a specified range of folder IDs.

Features:
- Each downloaded file is saved in a folder corresponding to its source (e.g., C:/I_CARE_dataset/0284/0284_EEG.txt).
- Files already present are skipped if the file size matches the remote version.
- During download, live progress and speed (KB/s) are shown in the terminal.
- Missing folders or files do not interrupt the process.
- All required directories are created automatically.

Requirements:
- Uses `requests` and `beautifulsoup4` libraries.
- Compatible with both Windows and Linux environments.

Author: musyasoz
Source data: https://physionet.org/files/i-care/2.1/training/

"""

import os
import requests
from bs4 import BeautifulSoup
import time

def download_eeg_files(base_url, target_folder, start=284, end=1020):
    for i in range(start, end + 1):
        folder_name = f"{i:04d}"
        folder_url = f"{base_url}/{folder_name}/"

        try:
            # Check if folder exists
            res = requests.get(folder_url, timeout=10)
            if res.status_code != 200:
                print(f"✗ Skipping (Folder not found): {folder_url}")
                continue

            # Parse page to find links containing '_EEG'
            soup = BeautifulSoup(res.text, "html.parser")
            links = soup.find_all("a")
            eeg_files = [link.get("href") for link in links if link.get("href") and "_EEG" in link.get("href")]

            for filename in eeg_files:
                file_url = folder_url + filename
                local_dir = os.path.join(target_folder, folder_name)
                os.makedirs(local_dir, exist_ok=True)
                local_path = os.path.join(local_dir, filename)

                # Check if file already exists and matches in size
                if os.path.exists(local_path):
                    local_size = os.path.getsize(local_path)
                    head = requests.head(file_url)
                    remote_size = int(head.headers.get("Content-Length", -1))

                    if local_size == remote_size:
                        print(f"✓ Already exists (skipped): {folder_name}/{filename}")
                        continue
                    else:
                        print(f"↺ Re-downloading (file differs): {folder_name}/{filename}")

                try:
                    r = requests.get(file_url, timeout=10)
                    if r.status_code == 200:
                        download_with_progress(file_url, local_path)
                    else:
                        print(f"✗ File not found: {file_url}")
                except Exception as e:
                    print(f"✗ Error downloading file: {file_url} — {e}")

        except Exception as e:
            print(f"✗ Error accessing folder: {folder_url} — {e}")

def download_with_progress(file_url, local_path):
    r = requests.get(file_url, stream=True, timeout=10)
    total_size = int(r.headers.get("Content-Length", 0))
    block_size = 1024  # 1 KB
    downloaded = 0
    start_time = time.time()

    with open(local_path, "wb") as f:
        for data in r.iter_content(block_size):
            f.write(data)
            downloaded += len(data)
            elapsed_time = time.time() - start_time
            speed = downloaded / elapsed_time if elapsed_time > 0 else 0
            percent = (downloaded / total_size) * 100 if total_size > 0 else 0
            print(f"\r⬇ {os.path.basename(local_path)} — {percent:5.1f}% | {speed/1024:6.1f} KB/s", end="")

    print(" ✓")  # Download complete


# Example usage:
base_url = "https://physionet.org/files/i-care/2.1/training"
target_folder = r"C:\I_CARE_dataset"  # Change this path as desired
download_eeg_files(base_url, target_folder, start=900, end=1020)
