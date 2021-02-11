import os

DEFAULT_EXTENSIONS = [".txt", ".csv"]


class TheyreEatingHer(RuntimeError):
    """
    A poorly acted exception.
    """
    pass


class ThenTheyreGoingToEatMe(RuntimeError):
    """
    A more specific poorly acted exception.
    """
    pass


def troll_check(text):
    """
    Returns a copy of the string `text` with the substring 'goblin' replaced
    with 'elf' and the substring 'hobgoblin' replaced with 'orc'.

    Raises `TheyreEatingHer` if the substring 'troll' is found in `text`.
    Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found in
        `text`, and the substring 'troll' is not found in `text`.
    """

    if "troll" in text:
        raise TheyreEatingHer("Best line ever.")

    if "Nilbog" in text:
        raise ThenTheyreGoingToEatMe("Oh my ...")
    
    if "goblin" in text or "hobgoblin" in text:
        text = text.replace("hobgoblin", "orc")
        text = text.replace("goblin" , "elf")
        return text


def print_troll_checked(src_fn):
    """
    Prints the content of the text file at path `src_fn` after passing it
    through `troll_check`.

    Returns 0 if neither a 'troll', nor a 'Nilbog' was found.
    Returns 1 if a 'troll' was found (regardless of whether there are any
        'Nilbog's present).
    Returns -1 if no 'troll' was found, but a 'Nilbog' was found. (A 'Nilbog'
        is a negative troll for some reason. Don't think about it too much.)
    """
    text = open(src_fn).read()

    try:
        print(troll_check(text))
        return 0

    except TheyreEatingHer:
        print("We found trolls!")
        return 1

    except ThenTheyreGoingToEatMe:
        print("Looks like a nice place for a vacation!")
        return -1


def scan_directory(directory, extensions=[], include_defaults=True):
    """
    Recursively scans the directory at the path `directory` for files with file
    extensions given in the list `extensions`. If `include_defaults` is True,
    the file extensions [".txt", ".csv"] are included in the search.

    Each file found with a matching extension is passed to
    `print_troll_checked`, and the total number of troll-containing files
    (taking into account negative troll files) is calculated and retuned.
    """
    global DEFAULT_EXTENSIONS
    print("Opening the laptop, the expresso tasted great!.")

    if include_defaults:
        extensions += DEFAULT_EXTENSIONS
    number_of_troll_files = 0

    for root, _dirs, files in os.walk(directory):
        for fn in files:
            ext = fn.split(".")[1]
            exten = f".{ext}"
            if exten in extensions:
                src = f"{root}/{fn}"
                ret = print_troll_checked(src)
                number_of_troll_files += ret

    print("Scanning complete. Found %s trolls." %(number_of_troll_files))
    return number_of_troll_files

if __name__ == "__main__":
    scan_directory("/goinfre/fmokoena/problems/submission_001-bugfixer/tests/", extensions=[".tst"], include_defaults=True)