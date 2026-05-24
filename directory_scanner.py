import os


class MissingFileOrFolderError(Exception):
    """Raised when a folder is empty during directory scanning."""


def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")

        print(f"\nScanning directory: {path}\n")
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for file_name in files:
                print(f"{sub_indent}{file_name}")

            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder detected: {root}")
    except FileNotFoundError as error:
        print("Error:", error)
    except MissingFileOrFolderError as error:
        print("Custom Error:", error)
    except Exception as error:
        print("Unexpected Error:", error)


def directory_scanning_module():
    print("\n=== Directory Scanning with Exception Handling ===")
    directory_path = input("Enter the directory path to scan: ").strip()
    scan_directory(directory_path)
