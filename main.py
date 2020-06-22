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
    # append the author and title in case they are not there. Should I use set?
    if "author" not in required_fields: required_fields.append("author")
    if "title" not in required_fields: required_fields.append("title")

    for entry in bibtex_database.entries:
        missing_items = []
        for item in required_fields:
            if item not in entry:
                print(entry["ID"], " is missing ", item)
                missing_items.append(item)
        if len(missing_items)!= 0:
            ret.append([entry["ID"],missing_items])

    return ret

def clean_up_names(bib_item):
    """Leverages on bibtexparser and turns names into lists"""
    for items in bib_item.entries:
        bibtexparser.customization.author(items)

# this is quite possibly the ugliest piece of code I've ever written...
def print_all_names(bib_item):
    for idx, names in enumerate(bib_item['author']):
        if idx > 0:
            if idx != len(bib_item['author'])-1:
                print(", ",  sep='', end ="")
            else:
                print(" and ", sep='', end ="")
        print(bibtexparser.customization.splitname(names)['first'][0]," ", bibtexparser.customization.splitname(names)['last'][0], sep='', end ="")

