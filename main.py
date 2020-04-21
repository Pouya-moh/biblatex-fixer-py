import bibtexparser

def load_bibtex_database(file_name):
    """Loads a .bib 
    
    :param file_name: path to file
    :returns: a bibtex database
    """
    with open(file_name) as bibtex_file:
        return bibtexparser.loads(bibtex_file.read())

