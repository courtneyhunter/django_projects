import csv

# python3 manage.py shell < many/load.py

from unesco.models import site, category, iso, region, states

fhand = open('unesco/whc-sites-2018-small.csv')
reader = csv.reader(fhand)

site.objects.all().delete()
category.objects.all().delete()
iso.objects.all().delete()
region.objects.all().delete()
states.objects.all().delete()

z = 0
for row in reader:
    if z > 0:
        try:
            name = site.objects.get(name=row[0])
        except:
            print("Inserting name",row[0])
            # name = site(name=row[0])
            # name.save()

        try:
            desc = site.objects.get(description=row[1])
        except:
            print("Inserting description",row[1])
            # desc = site(description=row[1])
            # desc.save()

        try:
            just = site.objects.get(justification=row[2])
        except:
            print("Inserting justification",row[2])
            # just = site(justification=row[2])
            # just.save()

        try:
            year = site.objects.get(year=row[3])
        except:
            print("Inserting year",row[3])
            # year = site(year=row[3])
            # year.save()

        try:
            long = site.objects.get(longitude=row[4])
        except:
            print("Inserting longitude",row[4])
            # long = site(longitude=row[4])
            # long.save()

        try:
            lat = site.objects.get(latitude=row[5])
        except:
            print("Inserting latitude",row[5])
            # lat = site(latitude=row[5])
            # lat.save()

        try:
            area = site.objects.get(area_hectares=row[6])
        except:
            print("Inserting area_hectares",row[6])
            # area = site(area_hectares=row[6])
            # area.save()

        try:
            y = int(row[3])
        except:
            y = None
        try:
            l = float(row[4])
        except:
            l = None
        try:
            la = float(row[5])
        except:
            la = None
        try:
            a = float(row[6])
        except:
            a = None

        # save1 = site(name=row[0], description=row[1], justification=row[2],
        #                     year=y, longitude=lo, latitude=lat, area_hectares=ah)
        # save1.save()

        try:
            c = category.objects.get(name=row[7])
        except:
            #print("Inserting category",row[7])
            c = category(name=row[7])
            c.save()

        try:
            st = states.objects.get(name=row[8])
        except:
            #print("Inserting states",row[8])
            st = states(name=row[8])
            st.save()

        try:
            r = region.objects.get(name=row[9])
        except:
            #print("Inserting region",row[9])
            r = region(name=row[9])
            r.save()

        try:
            q = iso.objects.get(name=row[10])
        except:
            #print("Inserting iso",row[10])
            q = iso(name=row[10])
            q.save()

        s = site(name=row[0], description=row[1], justification=row[2],
                 year=y, longitude=l, latitude=la, area_hectares=a,
                 category=c, state=st, region=r, iso=q)
        s.save()
    z += 1
