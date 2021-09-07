import sys
import logging
import rds_config
import pymysql
import json
import datetime

# rds settings
rds_host = "haniumtrafficlight.cbk0vfgjfbad.us-east-2.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def json_default(value):
    if isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d')
        raise TypeError('not JSON serializable')

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    sys.exit()
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    with conn.cursor() as cur:
        data = json.dumps(event)
        data1 = json.loads(data)['body']
        a = str(data1["user_id"])
        b = str(data1["name"])
        c = str(data1["birth"])
        d = str(data1["weak_name"])
        cur.execute(f"select EXISTS (select * from logindb where user_id = '{a}' ) as success")
        for Device in cur.fetchall() :
            dev = Device[0]
        if dev:
            return 'already exists this user'
        cur.execute(f"""INSERT INTO `trafficappdb`.`logindb` (`user_id`, `name`, `birth`, `weak_name`) VALUES ('{a}', '{b}', '{c}', '{d}')""")
 
    conn.commit()
    return 'uploaded %s in the db' % a
