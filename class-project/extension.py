import os


def changeFileExtensions(folderPath, newFileType):
    """This function renames all files in a folder by changing their extensions to a desired one.

    Args:
    folderPath (str): The path to the folder containing the files to be renamed.
    newFileType (str): The new file extension (including the dot). For example: '.csv'
    """

    folder = os.path.expanduser(folderPath)
    files = os.listdir(folder)

    for file in files:
        fileName, _ = os.path.splitext(file)
        src = os.path.join(folder, file)
        dst = os.path.join(folder, fileName + newFileType)
        os.rename(src, dst)
