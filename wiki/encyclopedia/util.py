import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

#Added function to check whether title is in entries
def is_title_valid(title):
    """
    Loops through articles stored and if title matches title of article returns True, False otherwise. Case sensitive
    """
    entries = list_entries()
    for entry in entries:
        if entry == title:
            return True

    return False

#Added function
def regex_article_match(regex):
    """
    Goes through articles and returns list of articles that contain regex passed in as a substring
    """
    result = []
    #Get list of entries and loop over them
    for entry in list_entries():
        #Check if regex expression matches
        if re.search(regex, entry, re.IGNORECASE):
            #If it does get entry and add to result
            result.append(entry)
    return result