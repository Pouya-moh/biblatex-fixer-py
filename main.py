import bibtexparser

def load_bibtex_database(file_name):
    """
    Loads a .bib 
    
    :param file_name: path to file
    :returns: a bibtex database
    """
    with open(file_name) as bibtex_file:
        return bibtexparser.loads(bibtex_file.read())

def check_incomplete_entries(bibtex_database, required_fields):
    """
    checks if all the entries insided the passed database contain
    requried fields. Note that "title" and "author" are checked 
    regardless and don't need to be passed.
    
    :param bibtex_database: 
    :param required_fields: list of minimum fields, e.g., ["doi", "pages", "year"]
    :returns: a list of entries (by id) where an item is missing
    """
    ret = []
    # append the author and title in case they are not there.
    if "author" not in required_fields: required_fields.append("author")
    if "title" not in required_fields: required_fields.append("title")

    for entry in bibtex_database.entries:
        for item in required_fields:
            if item not in entry:
                print(entry["ID"], " is missing ", item)
                ret.append(entry["ID"])

    # TODO return list of lists!
    return ret

