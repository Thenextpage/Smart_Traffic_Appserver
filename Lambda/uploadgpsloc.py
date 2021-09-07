import sys
import logging
import rds_config
import pymysql
import json
import datetime
#rds settings
rds_host  = "haniumtrafficlight.cbk0vfgjfbad.us-east-2.rds.amazonaws.com"
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
        data1= json.loads(data)['body']
        a   = float(str(data1["latitude"]))
        b   = float(str(data1["longitude"]))
        c   = str(data1["user_id"])
        
        cur.execute(f"""insert into `trafficappdb`.`gpslocation` (`latitude`, `longitude`,`user_id`) values({a},{b},"{c}") ON DUPLICATE KEY UPDATE longitude={b},latitude={a}""")
    conn.commit()

    return 
