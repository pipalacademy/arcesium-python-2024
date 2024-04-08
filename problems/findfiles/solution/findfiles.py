import os


def findfiles(folderpath, prefix, extension):
    allfiles = os.listdir(folderpath)
    filtered = []

    for file in allfiles:
        if file.startswith(prefix) and file.endswith(extension):
            filtered.append(file)

    return filtered
