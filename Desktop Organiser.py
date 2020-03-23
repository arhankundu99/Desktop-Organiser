import os
from pathlib import Path

DIRECTORIES = {
    "HTML": (".html5", ".html", ".htm", ".xhtml"),
    "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".png"),
    "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".mpg", ".mpeg", ".3gp"),
    "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                   ".xls", ".xlsx", ".ppt",
                  "pptx"),
    "ARCHIVES": (".iso", ".xar", ".zip"),
    "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
    "PLAINTEXT": (".txt", ".in", ".out"),
    "PDF": ".pdf",
    "XML": ".xml",
    "EXE": ".exe",
    "SHELL": ".sh",
}
# swapping keys and values of directories dictionaries
FILE_FORMATS = dict([(value, key) for key, value in DIRECTORIES.items()])


def organize_files():
    for entry in os.scandir():
        file_path = Path(entry)
        print(file_path)
        if entry.is_dir():
            dirContents = os.listdir(file_path)
            # if there are no contents in the folder, delete the folder
            if len(dirContents)==0:
                os.removedirs(file_path)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

organize_files()
