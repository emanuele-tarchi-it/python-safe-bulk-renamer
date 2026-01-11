__version__ = "1.0.0"
__author__ = "Emanuele Tarchi"

import os

def rename_files(folder_path, prefix="", suffix="", replace_from="", replace_to="", target_ext=None, dry_run=True):
    """
    Renames files in a specific folder with safety checks and filters.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    files = os.listdir(folder_path)
    counter = 1
    
    print(f"{'--- DRY RUN MODE (No changes applied) ---' if dry_run else '--- LIVE MODE (Executing changes) ---'}")

    for filename in files:
        old_path = os.path.join(folder_path, filename)

        # Skip directories
        if not os.path.isfile(old_path):
            continue
            
        name, ext = os.path.splitext(filename)
        
        # Filter by extension if specified (e.g., '.jpg')
        if target_ext and ext.lower() != target_ext.lower():
            continue

        # Renaming logic
        new_name = name.replace(replace_from, replace_to)
        new_name = f"{prefix}{new_name}{suffix}_{counter}{ext}"
        new_path = os.path.join(folder_path, new_name)

        if dry_run:
            print(f"[Preview] {filename}  -->  {new_name}")
        else:
            # Safety: Do not overwrite existing files
            if os.path.exists(new_path):
                print(f"[Skipped] {new_name} already exists.")
            else:
                os.rename(old_path, new_path)
                print(f"[Success] {filename} renamed.")
        
        counter += 1

    if dry_run:
        print("\nDry run complete. Set dry_run=False to apply these changes.")

if __name__ == "__main__":
    # Example usage
    rename_files(
        folder_path="your_folder_here", 
        prefix="PROJECT_", 
        replace_from=" ", 
        replace_to="_",
        target_ext=".pdf", # Optional: filter by extension
        dry_run=True       # Toggle to False when ready
    )
