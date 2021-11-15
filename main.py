import psycopg2

username = "postgres"
password = "admin"
database = "formula1_DB"
host = "localhost"
port = "5432"

query_1 = '''
select TRIM(drivername.driver_id), TRIM(driver_forename), TRIM(driver_surname), points
from drivername join results on (Drivername.driver_id = Results.driver_id)
where points > 9
'''

query_2 = '''
select TRIM(driver_forename), TRIM(driver_surname), points
from Drivername join Results on (Drivername.driver_id = Results.driver_id)
'''

query_3 = '''
select TRIM(Drivername.driver_id), points
from Drivername join Results on (Drivername.driver_id = Results.driver_id)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with conn:

    print("Database opened successfully")

    cur = conn.cursor()

    print('1.')

    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.')

    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.')

    cur.execute(query_3)
    for row in cur:
        print(row)
