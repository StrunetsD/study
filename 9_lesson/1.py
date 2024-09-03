import glob
import os
import shutil

def main():
    print(f"name OS: {os.name}")
    print(f"path: {os.getcwd()}")

    extensions = {
        "txt": "txt_files",
        "html": "html_files"
    }

    for extension, folder in extensions.items():
        files = glob.glob(os.path.join(os.getcwd(), f"*.{extension}"))
        print(f"{len(files)} file(s) with extension .{extension}")

        folder_path = os.path.join(os.getcwd(), folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        size = 0

        for file in files:
            basename = os.path.basename(file)
            destination_path = os.path.join(folder_path, basename)
            shutil.move(file, destination_path)
            size += os.path.getsize(destination_path)

        if files:
            first_file = os.path.join(folder_path, os.path.basename(files[0]))
            new_name = "new"
            new_path = os.path.join(folder_path, new_name)
            os.rename(first_file, new_path)
            print(f"file {os.path.basename(first_file)} was renamed in {new_name}")
        if files:
            print(f"{folder} move {len(files)}, total size = {size / (1024 ** 3):.2f} ГБ")

if __name__ == "__main__":
    main()