# Python Bulk File Renamer

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

A robust and safe command-line utility to rename multiple files at once. Designed with a "Safety First" approach for professionals managing large datasets, photos, or documents.

## 🚀 Key Features
- **Dry Run Mode:** Preview all changes before they are actually applied to your files.
- **Collision Protection:** Automatically skips renaming if the target filename already exists to prevent data loss.
- **Extension Filtering:** Choose to rename only specific file types (e.g., only `.jpg` or `.pdf`).
- **Flexible Logic:** Add prefixes, suffixes, or perform text replacement within filenames.

## 🛠 How to Use
1. Clone the repository to your local machine.
2. Open `renamer.py`.
3. Configure the `rename_files` function parameters in the `if __name__ == "__main__":` block:
   - `folder_path`: The directory containing your files.
   - `prefix` / `suffix`: Text to add at the start or end.
   - `target_ext`: Filter by extension (e.g., ".txt").
   - `dry_run`: Set to `True` for testing, `False` for execution.
4. Run the script: `python renamer.py`

## 📄 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
*Developed by Emanuele Tarchi | Automation Specialist Portfolio*
