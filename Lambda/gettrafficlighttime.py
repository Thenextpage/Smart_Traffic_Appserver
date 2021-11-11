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
        return value.strftime('%Y-%m-%d %H:%M:%S')
        raise TypeError('not JSON serializable')


try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


def lambda_handler(event, context):
    with conn.cursor(pymysql.cursors.DictCursor) as cur:

        try:
            cur.execute(f"""select * from time_table where (updatetime > DATE_ADD(NOW(),INTERVAL 537 minute)) """)
            datas = json.dumps(cur.fetchall(), default=json_default)
            conn.commit()
        except Exception as e:
            return e

    return {"lights":json.loads(datas)}
