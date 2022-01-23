# Wrangle_OpenStreetMap_MichelleBeckner
Data Wrangling with MongoDB – C750 Project

FILES CREATED AND USED
1. audit.py - discover the number of various elements in the file
2. tags.py – discover the type and number of tags in the file
3. audit_city_names.py – discover the city names in the file
4. audit_street_names.py – discover the street names in the file
5. update.py - make suggested updates to the city and street names
6. data.py - clean the city and street name data and convert the data into csv files 
7. create_db.py – create database from csv files
8. queries.py – sql scripts to query the database


EXPLORING AND CLEANING THE DATA

I used Open Street Maps to export map data for my current town of Spartanburg, South Carolina. Using Python, I wanted to examine the data that was pulled. 

The OSM file contain three main elements: nodes, ways, and relations. I used the file audit.py to discover the number of various elements in the file:

 'bounds': 1,
 'member': 9897,
 'meta': 1,
 'nd': 951091,
 'node': 824349,
 'note': 1,
 'osm': 1,
 'relation': 475,
 'tag': 822676,
 'way': 127549}

I found that “member”, “nd” and “tag” also had a large number of occurrences. According to Wikipedia, “XML elements tag, nd, and member are not referred to as elements in OSM XML but they are indeed XML elements.”

I then wanted to see the number of tags in the elements. I used tags.py to audit the data for this information. I discovered the various tags:

[('addr:street', 105746),
 ('addr:city', 105706),
 ('addr:postcode', 105656),
 ('addr:housenumber', 105655),
 ('addr:state', 105605),
 ('building', 82863),
 ('highway', 40743),
 ('service', 15404),
 ('addr:unit', 12669),
 ('name', 11709),
 ('surface', 10721),
 ('access', 7251),
 ('tiger:county', 6272),
 ('tiger:cfcc', 6211),
 ('tiger:name_base', 5992),
 ('footway', 5921),
 ('tiger:name_type', 5594),
 ('tiger:zip_left', 4550),
 ('tiger:zip_right', 4391),
 ('crossing', 3840),
 ('source', 3669),
 ('amenity', 2996),
 ('power', 2877),
 ('oneway', 2374),
 ('landuse', 2298),
 ('tiger:name_base_1', 1999),
 ('building:levels', 1910),
 ('NHD:FCode', 1904),
 ('NHD:ReachCode', 1851),
 ('NHD:ComID', 1800),
 ('NHD:RESOLUTION', 1781),
 ('waterway', 1603),
 ('name_1', 1581),
 ('barrier', 1551),
 ('NHD:FType', 1442),
 ('NHD:way_id', 1440),
 ('lanes', 1398),
 ('parking', 1390),
 ('attribution', 1323),
 ('natural', 1319),
 ('maxspeed', 1081),
 ('leisure', 1043),
 ('fee', 954),
 ('ref', 930),
 ('website', 912),
 ('place', 856),
 ('direction', 790),
 ('phone', 767),
 ('lit', 748),
 ('railway', 738),
 ('tiger:name_direction_prefix_1', 704),
 ('gnis:feature_id', 669),
 ('layer', 509),
 ('entrance', 506),
 ('tiger:name_direction_prefix', 502)]

I wanted to look at the city names in Spartanburg to be sure they were correct. I used Wikipedia to get a list of the city names I expected to see. Using the audit_city_names.py file, I discovered the following additional city names:

{'Arcadia': {'Arcadia'},
 'Campobello': {'Campobello'},
 'Converse': {'Converse'},
 'Cowpens': {'Cowpens'},
 'Drayton': {'Drayton'},
 'Duncan': {'Duncan'},
 'Glendale': {'Glendale'},
 'Greer': {'Greer'},
 'Lyman': {'Lyman'},
 'Moore': {'Moore'},
 'Reidville': {'Reidville'},
 'Roebuck': {'Roebuck'},
 'Springs': {'Boiling Springs'},
 'Startex': {'Startex'},
 'Una': {'Una'},
 'Welford': {'Welford'}}

I reviewed these names with Wikipedia and discovered that they were listed as towns or census designated places. Therefore, I will accept them as clean data with the exception of Welford. Welford is a misspelling for Wellford and needs to be corrected. 

Next, I wanted to see is the street names were consistent in naming of street types. I used audit_street_names.py to look at the street names. The following observations were encountered:

1.  Some street names end in numbers such as Highway 56 and Interstate 85. These are acceptable as they are correct names of highways and interstates.

2. There is inconsistency in how some road names are reported such as ‘St’ instead of ‘Street’, ‘Dr’ instead of ‘Drive’, ‘Cir’ instead of ‘Circle’. I will want to correct these so naming in consistent. 

3. Some roads in the Hillcrest neighborhood have the name of the neighborhood listed in the street name such as ‘Rosewood St Hillcrest’. I want to remove the name of the neighborhood from the street name. 

I used update.py to make the suggested updates to the city and street names. The file contained a script to verify the name changes. 

DATABASE CREATION AND ANALYSIS

I used data.py to clean the city and street name data and convert the data into csv files that could be imported into a sql database. 

I used create_db.py to create my database and load the newly created csv files into it. The file contained a script to count the number of nodes and ways. This count was compared to the count done on the osm file in the beginning of my analysis to verify that all the information was transferred over to the database.

I used the queries.py file to run some analysis sql queries on the Spartanburg database. 

The results of the queries were:
1. Number of nodes:  824349
2. Number of ways:  127549
3. Number of unique users:  779
4. Name and number of different religions:  [('christian', 43), ('jewish', 1)]
5. Name and number of different cuisines:  [('mexican', 11), ('pizza', 8), ('burger', 7), ('american', 6), ('sandwiches', 5), ('regional', 5), ('japanese', 5), ('breakfast', 5), ('barbecue', 5), ('southern', 4), ('chinese', 4), ('thai', 3), ('sushi', 3), ('sandwich', 3), ('wings', 2), ('tapas', 2), ('steak', 2), ('salads', 2), ('jamaican', 2), ('italian', 2), ('hot_dog', 2), ('deli', 2), ('chicken', 2), ('asian', 2), ('vietnamese', 1), ('subs', 1), ('steak_house', 1), ('smoothies', 1), ('seafood', 1), ('pub', 1), ('local', 1), ('juice', 1), ('indian', 1), ('german', 1), ('drinks', 1), ('doughnuts', 1), ('donuts', 1), ('crepes', 1), ('crepe', 1), ('coffee_shop', 1), ('caribbean', 1), ('bar&grill', 1), ('bagels', 1)]

IMPROVEMENT

An area for improvement would be in the area of places of religion. Spartanburg is in the south and part of what used to be known as the Bible Belt. As such I would expect more places of worships. I also find it not believable that there is only 1 other type of religion. Updating the information would have to include more data analysis to see if these results are just indication if the data needs to be cleaned better or if more data needs to be added to the OpenStreetMap itself. The difficulty would be in assessing how to acquire the information on the different places of worship not already listed. 


REFERENCES

https://gist.github.com/swwelch/f1144229848b407e0a5d13fcb7fbbd6f 
https://en.wikipedia.org/wiki/Spartanburg_County,_South_Carolina
https://en.wikipedia.org/wiki/Bible_Belt
https://python2to3.com/
https://wiki.openstreetmap.org/wiki/Elements#Elements
https://github.com/AdkinsWx/OpenStreetMap_Udacity/blob/master/Final_Code.ipynb
https://hadrien-lcrx.github.io/notebooks/Boston_Data_Wrangling.html
https://github.com/mspbannister/dand-p3-openstreetmap/blob/master/update.py






