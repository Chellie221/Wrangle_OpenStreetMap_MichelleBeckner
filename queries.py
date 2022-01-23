import sqlite3


def number_of_nodes():
    result = cur.execute('SELECT COUNT(*) FROM nodes')
    return result.fetchone()[0]


def number_of_ways():
    result = cur.execute('SELECT COUNT(*) FROM ways')
    return result.fetchone()[0]


def number_of_Unique_users():
    result = cur.execute('SELECT COUNT(distinct(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways)')
    return result.fetchone()[0]


def number_religions():
    result = cur.execute('SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id) '
                         'FROM nodes_tags WHERE value="place_of_worship") i ON nodes_tags.id=i.id '
                         'WHERE nodes_tags.key="religion" GROUP BY nodes_tags.value ORDER BY num DESC;')
    return result.fetchall()


def number_cuisine():
    result = cur.execute('SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id) '
                         'FROM nodes_tags WHERE value="restaurant") i ON nodes_tags.id=i.id '
                         'WHERE nodes_tags.key="cuisine" GROUP BY nodes_tags.value ORDER BY num DESC;')
    return result.fetchall()


if __name__ == '__main__':
    con = sqlite3.connect("spartanburg.db")
    cur = con.cursor()
    print("Number of nodes: ", number_of_nodes())
    print("Number of ways: ", number_of_ways())
    print("Number of unique users: ", number_of_Unique_users())
    print("Name and number of different religions: ", number_religions())
    print("Name and number of different cuisines: ", number_cuisine())