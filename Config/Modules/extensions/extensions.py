"""
A program that prompts the user for the name of a file and
then outputs that file's media type if the file's name ends.
"""

file = input("Filename: ").strip()

extensions = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]

no_extension = "application/octet-stream"

file_type = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

not_found = None
for ext in extensions:
    if file.lower().endswith(ext):
        not_found = ext
        break

if not_found:
    print(f"{file_type[not_found]}")
else:
    print(f"{no_extension}")
