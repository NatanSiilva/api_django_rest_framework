from datetime import datetime

def validate_files(request, field, update=False):
    request = request.copy()

    if update:
        if type(request[field]) == str: request.__delitem__(field)
    else:
        if type(request[field]) == str: request.__setitem__(field, None)        

    return request

def validate_files01(request, field, update=False):
    request._mutable = True

    if update:
        if type(request[field]) == str:
            del request[field]
    else:
        request[field] = None if type(request[field]) == str else request[field]
        
    request._mutable = False

    return request



def format_date(date):
    date = datetime.strptime(date, '%d/%m/%Y')
    date = f"{date.year}-{date.month}-{date.day}"
    return date
