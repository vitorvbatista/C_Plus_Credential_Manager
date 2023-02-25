# CREATE CS+ database with AUTHENTICATION table
# As the same, a table called PASS will be created to
# Insert into AUTHENTICATION a generic password (common_auth)

import sqlite3

conn = sqlite3.connect('CS+')
c = conn.cursor()

# c.execute('''
#           CREATE TABLE IF NOT EXISTS AUTHENTICATION
#             ([auth_id] INTEGER PRIMARY KEY,
#             [auth_name] TEXT,
#             [auth_plain] TEXT)
#           ''')
#
# c.execute('''
#           CREATE TABLE IF NOT EXISTS PASS
#             (pass_id INTEGER PRIMARY KEY,
#              pass_name TEXT,
#              pass_user TEXT,
#              pass_plain TEXT,
#              pass_observation TEXT,
#              pass_expiry_date DATE)
#           ''')
#
# c.execute('''
#           INSERT INTO AUTHENTICATION (auth_id, auth_name, auth_plain)
#                 VALUES
#                 (1,'common_authentication', 'common_auth')
#           ''')

# conn.commit()
