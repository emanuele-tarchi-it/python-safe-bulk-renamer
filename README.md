# Python Bulk File Renamer
**Version 1.0.0** | **License: MIT**

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
This project is licensed under the **MIT License** - see the LICENSE file for details. This means you are free to use, modify, and distribute it for personal or commercial projects.

---
*Developed by Emanuele Tarchi as part of a Python Automation Portfolio.*
