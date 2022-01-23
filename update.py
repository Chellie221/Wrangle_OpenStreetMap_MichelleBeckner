import re

from numpy.distutils.fcompiler import none

FILENAME = 'map.osm'

st_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
city_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

mapping = {'Ave':'Avenue',
        'Cir':'Circle',
        'Ln':'Lane',
        'St':'Street',
        'St Hillcrest': 'Street',
        'Ln North': 'Lane North',
        'Ln South': 'Lane South',
        'Simuel Road;Hearon Cir': 'Simuel Road',
        'W': 'West'
        }

mapping2 = {'Welford': 'Wellford'}

def update_st_name(value):
    m = st_type_re.search(value)
    if m:
        if m.group() in mapping:
            startpos = value.find(m.group())
            value = value[:startpos] + mapping[m.group()]
        return value
    else:
        return None

def update_city_name(value):
    m = city_type_re.search(value)
    if m:
        if m.group() in mapping2:
            startpos = value.find(m.group())
            value = value[:startpos] + mapping2[m.group()]
        return value
    else:
        return none

def update_value(value, key):
    if key == 'addr:street':
        return update_st_name(value)
    elif key == "addr:city":
        return update_city_name(value)
    else:
        return value

def update_type(key):
    if ":type" in key:
         pass
    elif "_type" in key:
         key = key[:(key.find("_type"))] + ":type"
    elif "type" in key and key.find("type") != 0:
         key = key[:(key.find("type"))] + ":type"
    return key
