import re
import sys
import xlrd


def get_sheet(excel_fname, sheet_name=None):
    """
    Get sheet specified in `sheet_name` from excel file `excel_fname`.
    """
    book = xlrd.open_workbook(excel_fname)

    if sheet_name:

        if sheet_name in book.sheet_names():
            sheet = book.sheet_by_name(sheet_name)
            return sheet
        else:
            print("ERROR: Sheet '{0}' cannot be found in workbook '{1}'".format(
                   sheet_name, excel_fname))
            sys.exit(1)

    else:
        # Get the first worksheet.
        sheet = book.sheet_by_index(0)
        return sheet


def get_row_slice(xlrd_sheet, start_row):
    """
    Generates row slices of given xlrd.sheet.Sheet
    starting from row # `start_row`.
    """
    num_rows = xlrd_sheet.nrows

    for _ in range(num_rows):
        # print start_row
        yield xlrd_sheet.row_slice(rowx=start_row, start_colx=0, end_colx=3)
        start_row += 1


def check_code(item_code):
    """
    Checks whether given `item_code` is proper.
    """
    # RA matches
    if re.match(r'^MCRNC[0-9]{4}\.T$', item_code):
        return True

    if re.match(r'^RAN[0-9]{3,4}(\.[0-9])?C?(\.T)?$', item_code):
        return True

    if re.match(r'^RAS[0-9]{5}$', item_code):
        return True

    if re.match(r'^RNC[0-9]{4}\.T$', item_code):
        return True

    if re.match(r'^RU[0-9]{5}(\.T)?$', item_code):
        return True

    # Feature ID (RAN) matches
    if re.match(r'^RAN[0-9]{2,5}$', item_code):
        return True

    if re.match(r'^(?P<code>RAN[1,2](\.[0-9]{3,4}))$', item_code):
        return True

    return False


def parse_sheet(xlrd_sheet):
    """
    Returns dict representation of given sheet.
    """
    res_dict = {}
    ra_item = None

    for row_slice in get_row_slice(xlrd_sheet, start_row=0):
        item_code, descr, f_id = row_slice

        # Instantiate appropriate sales items.
        # 0=Empty
        # 1=Text
        if item_code.ctype == 1:

            if check_code(item_code.value):
                ra_item = SalesItem(item_code.value, descr.value)
                res_dict[ra_item] = []
            else:
                continue

        if f_id.ctype == 0:
            continue
        elif f_id.ctype == 1:
            ran_item = SalesItem(f_id.value, descr.value)
            # Fill the dict.
            res_dict[ra_item].append(ran_item)

    return res_dict


def get_file_data(upl_file_obj, fname):
    """
    Takes UploadedFile object and returns a list
    of item codes it contains.
    """
    res_lst = []

    # Check whether given file is an EXCEL file.
    match_obj = re.match(r'^[\w]+\.xls[xm]?$', fname)
    if not match_obj:
        return res_lst

    # Write file to media/tmp/
    from django.core.files.storage import default_storage

    with open(default_storage.path('tmp/' + fname), 'wb+') as destination:
        for chunk in upl_file_obj.chunks():
            destination.write(chunk)

    # Fetch data from file.
    sheet = get_sheet('media/tmp/' + fname)
    column = sheet.col(0)  # grab 1st col
    for item in column:
        res_lst.append(item.value)

    # !!!TODO: consider removing files from media/tmp/

    return res_lst


class SalesItem(object):

    def __init__(self, code, description=None):
        self._code = code
        self._descr = description

    def __repr__(self):
        return '<Sales Item: {}>'.format(self._code)

    def __hash__(self):
        return hash(self._code)

    def __eq__(obj1, obj2):
        return obj1.__hash__() == obj2.__hash__()

    def get_code(self):
        return self._code

    def get_description(self):
        return self._descr


#######################################################################
# Actual parsing. (Time being solution with hardcodded path).

# !!!TODO: consider usage of only one func
#          make things smarter.

def parse_ra():
    """
    RA -> RAN mapping.
    """
    fname = 'parse/File1.xlsx'
    sheet_name = 'Sheet1'

    ra_sheet = get_sheet(fname, sheet_name)
    return parse_sheet(ra_sheet)


def parse_f_id():
    """
    RAN -> OSS mapping.
    """
    fname = 'parse/File2.xlsx'
    sheet_name = 'Sheet1'

    ran_sheet = get_sheet(fname, sheet_name)
    return parse_sheet(ran_sheet)
