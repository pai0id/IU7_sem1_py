def stud(fields, widths=None):
    if widths is None:
        widths = [0, 0, 0, 0]
    name = fields[0].strip()
    year = fields[1].strip()
    res = fields[2].strip()
    passed = fields[3].strip()
    wname = widths[0]
    wyear = widths[1]
    wres = widths[2]
    wpassed = widths[3]
    return f"{name.center(wname)}|{year.center(wyear)}|{res.center(wres)}|{passed.center(wpassed)}"
