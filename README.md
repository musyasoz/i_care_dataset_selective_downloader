# 🧠 I-CARE EEG Dataset Downloader

This Python script allows selective downloading of EEG files (`_EEG`) from the [I-CARE v2.1 dataset](https://physionet.org/files/i-care/2.1/training/) hosted on [PhysioNet](https://physionet.org/). It is particularly useful for extracting only relevant files from a large collection of subject folders.

## 🔍 Overview

- ✅ Downloads EEG-related files from specified folder ranges (e.g., 0284 to 1060).
- ✅ Preserves the original folder structure (e.g., `target_folder/0284/0284_EEG.txt`).
- ✅ Skips already downloaded files by comparing file sizes.
- ✅ Displays download progress and live speed (KB/s) for each file.
- ✅ Automatically handles missing folders or files.
- ✅ Works on Windows, Linux, and WSL environments.

## 🚀 Requirements

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

## 🧩 Usage

Example usage in a Python script:

```python
from your_downloader_script import download_eeg_files

base_url = "https://physionet.org/files/i-care/2.1/training"
target_folder = r"C:\I_CARE_dataset"
download_eeg_files(base_url, target_folder, start=900, end=1060)
```

> ⚙️ Make sure to set the `target_folder` to your desired local directory.

## 📁 Output Structure

The script will create a directory structure like this:

```
C:/
└── I_CARE_dataset/
    ├── 0900/
    │   └── 0900_EEG.txt
    ├── 0901/
    │   └── 0901_EEG.txt
    └── ...
```

## ⚠️ Notes

- This script downloads only files that contain `_EEG` in their names.
- If a file already exists, it will only be re-downloaded if the file size differs from the remote version.

## 📜 License

You can freely use and change the code.

---

Created by musyasoz from neuronauts(https://github.com/musyasoz)
