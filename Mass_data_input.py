import pandas as pd
import sqlite3
from cryptography.fernet import Fernet
from datetime import datetime


data = pd.read_excel('YOUR PATH HERE')


for index, row in data.iterrows():

    key = b'26XVYFv-85Q_ESbCiY3-ag-LS2TwQBbyKWKxV9YQ-EY='
    fernet = Fernet(key)
    row['pass_plain'] = fernet.encrypt(row['pass_plain'].encode())
    row['pass_plain'] = row['pass_plain'].decode("utf8")

    row['pass_expiry_date'] = datetime.strptime(row['pass_expiry_date'], '%d/%m/%Y').date()

    conn = sqlite3.connect('CS+')
    c = conn.cursor()

    c.execute(f"""
              INSERT INTO PASS (pass_name, pass_user, pass_plain, pass_observation, pass_expiry_date)
                    VALUES
                    ('{row['pass_name']}',
                     '{row['pass_user']}',
                     '{row['pass_plain']}',
                     '{row['pass_observation']}',
                     '{row['pass_expiry_date']}')
              """)

    conn.commit()
