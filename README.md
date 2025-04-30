# i_care_dataset_selective_downloader

# 🧠 I-CARE EEG Dataset Selective Downloader

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
