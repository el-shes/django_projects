import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # 0name,1description, 2justification, 3year, 4longitude, 5latitude, 6area, 7category, 8state, 9region, 10iso

    for row in reader:
        # print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        i, created = Iso.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])

        y = try_int(row[3])

        a = try_float(row[6])
        lat = try_float(row[5])
        lon = try_float(row[4])

        m = Site(name=row[0], year=y, latitude=lat, longitude=lon, description=row[1], justification=row[2],
                 area_hectares=a, category=c, region=r, iso=i, state=s)
        m.save()


def try_int(value):
    try:
        y = int(value)
    except ValueError:
        y = None
    return y


def try_float(value):
    try:
        a = float(value)
    except ValueError:
        a = None
    return a
