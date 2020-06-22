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
def get_all_names(bib_item):
    for idx, names in enumerate(bib_item['author']):
        if idx > 0:
            if idx != len(bib_item['author'])-1:
                print(", ",  sep='', end ="")
            else:
                print(" and ", sep='', end ="")
        print(bibtexparser.customization.splitname(names)['first'][0]," ", bibtexparser.customization.splitname(names)['last'][0], sep='', end ="")


def print_authors(bib_item):
    print ('<span>', sep='',end="")
    get_all_names(bib_item)
    print (', </span>', sep='')

def print_month(bib_item):
    print('<span>',end="")
    print(bib_item['month'],end="")
    print(' </span>')

def print_year(bib_item):
    print('<span>',end="")
    print(bib_item['year'],end="")
    print(', </span>')

def print_publisher(bib_item):
    print(bib_item['publisher'],end="")

def print_journal(bib_item):
    print('<span><i>"',end="")
    print(bib_item['journal'],end="")
    print('", </i></span>', sep='')

def print_doi(bib_item):
    print('<span>DOI: ',end="")
    print('<a href="https://dx.doi.org/', sep='',end="")
    print(bib_item['doi'],'">', sep='',end="")
    print(bib_item['doi'],'</a>', sep='',end="")
    print('</span>')

def print_url(bib_item):
    print(bib_item['url'],end="")

def print_isbn(bib_item):
    print(bib_item['isbn'],end="")

def print_title(bib_item):
    print('<span><b>"',end="")
    print(bib_item['title'],end="")
    print('", </b></span>')

def print_abstract(bib_item):
    print(bib_item['abstract'],end="")

def print_pages(bib_item):
    print('<span>pp. ',end="")
    print(bib_item['pages'],end="")
    print(', </span>')

def print_entry(bib_item):
    print ('<p class="text-justify-sm">', sep='')
    print_authors(bib_item)
    print_title(bib_item)
    print_journal(bib_item)
    print_pages(bib_item)
    print_month(bib_item)
    print_year(bib_item)
    print_doi(bib_item)
    print ('</p>')
    abst_css='<div class="d-flex justify-content-between"><span style="font-variant: small-caps;text-rendering: auto;font-weight: bold;"><a class="text-dark collapsed" data-toggle="collapse" href="#collapseID_PAPER" role="button" aria-expanded="true" aria-controls="collapseID_PAPER">Abstract</a></span><a class="btn btn-outline-primary border-0 collapsed" data-toggle="collapse" href="#collapseID_PAPER" role="button" aria-expanded="true" aria-controls="collapseEducation"><i class="fa"></i></a></div><div class="collapse multi-collapse" id="collapseID_PAPER"><p class="text-justify-sm">'
    print (abst_css.replace("collapseID_PAPER","collapse_"+bib_item['ID']))
    print_abstract(bib_item)
    print('</p></div>')
    print('<hr class="mt-0" style="border-top: 3px double #8c8b8b;">')
