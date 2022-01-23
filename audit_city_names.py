import xml.etree.ElementTree as ET
from collections import defaultdict
import pprint
import re

osm_file = open("map.osm", "r")

city_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
city_types = defaultdict(set)

expected = ["Spartanburg", "Wellford", "Inman", "Chesnee", "Landrum",
            "Woodruff"]

def audit_city_type(city_types, city_name):
    m = city_type_re.search(city_name)
    if m:
        city_type = m.group()
        if city_type not in expected:
            city_types[city_type].add(city_name)

def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print("%s: %d" % (k, v))

def is_city_name(elem):
    return (elem.attrib['k'] == "addr:city")

def audit():
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_city_name(tag):
                    audit_city_type(city_types, tag.attrib['v'])
    pprint.pprint(dict(city_types))

if __name__ == '__main__':
    audit()