import re
import datetime
import os


def gettimestamp(stringce):
    izraz = re.compile(r'(.*?) \(((\d{2}.){2})-((\d{2}.){2})\)\.png')
    najdi = izraz.search(str(stringce))
    return datetime.datetime.strptime(najdi.group(2), "%d.%m.")


with os.scandir('.') as fajlovi:
    fajlovi2 = [i.name for i in fajlovi if '.png' in i.name]
    for i in sorted(fajlovi2, key=gettimestamp):
        print(i)
        a = re.sub(r'(.*?) Report (.*?)', r'\1 ReportMF \2', str(i))
        os.rename(i, a)
        print(a)
