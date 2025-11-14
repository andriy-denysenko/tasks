# Extension Extractor
# Given a string representing a filename, return the extension of the file.
#
# The extension is the part of the filename that comes after the last period (.).
# If the filename does not contain a period or ends with a period, return "none".
# The extension should be returned as-is, preserving case.

# Gets the extension of a given file name.
def get_extension(filename: str) -> str:
    extension: str = "none"
    found_pos: int = filename.rfind('.')
    if -1 < found_pos < len(filename) - 1:
        extension = filename[found_pos + 1:]
    return extension


assert (get_extension("document.txt") == "txt")
assert (get_extension("README") == "none")
assert (get_extension("image.PNG") == "PNG")
assert (get_extension(".gitignore") == "gitignore")
assert (get_extension("archive.tar.gz") == "gz")
assert (get_extension("final.draft.") == "none")