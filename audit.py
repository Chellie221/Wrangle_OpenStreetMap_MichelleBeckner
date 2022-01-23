import xml.etree.cElementTree as ET
import pprint

filename = "map.osm"

def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1

    return tags

tags = count_tags(filename)
pprint.pprint(tags)
