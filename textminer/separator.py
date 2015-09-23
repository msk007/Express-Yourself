import re

def date(s):
    x=re.match (r'(\d{1,2})/(\d{1,2})/(\d{4})', s)


    if m:
        return {'month':int(m.groups()[0]
        ),'day':int (m.groups()[1]), 'year':int (m.groups()[2])}
