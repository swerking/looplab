import os

def clean_filenames(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.wav') or filename.endswith('.aiff'):
            clean_name = filename.replace(' ', '_').lower()
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, clean_name)
            )
            print(f"Renamed: {filename} -> {clean_name}")

if __name__ == '__main__':
    folder = input("Enter the path to your loop folder: ")
    clean_filenames(folder)
