import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()
from mysite.models import Animal
import requests, json
url = "https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_area_pkid=16"
jsondata = requests.get(url).text
data = json.loads(jsondata)
for item in data:
    try:
        rec = Animal()
        rec.aid = item['animal_id']
        rec.place = item['animal_place']
        rec.kind = item['animal_kind']
        if item['animal_sex']=="M":
            rec.sex = True
        rec.status = item['animal_status']
        rec.remark = item['animal_remark']    
        rec.update = item['animal_update'].replace("/", "-")
        rec.album = item['album_file']
        rec.save()
    except Exception as e:
        print(e)
        pass
print("Done")