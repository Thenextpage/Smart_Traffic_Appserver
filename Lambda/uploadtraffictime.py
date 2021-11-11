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
        a   = str(event["greentime"])
        b   = str(event["redtime"])
        c   = event["latitude"]
        d   = event["longitude"]
        
        try:
            cur.execute(f"""insert into `trafficappdb`.`time_table` (`greentime`, `redtime`,`latitude`,`longitude`,`updatetime`) values("{a}","{b}",{c},{d},"DATE_ADD(NOW(),INTERVAL 9 hour)") ON DUPLICATE KEY UPDATE redtime="{b}",greentime="{a}",updatetime=DATE_ADD(NOW(),INTERVAL 9 hour) """)
            conn.commit()
        except Exception as e:
            return e
    return
