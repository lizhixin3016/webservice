import config
import pymysql


def getDevicesConn():
    conn = pymysql.connect(host=config.devices_db_host,
                           port=int(config.devices_db_port),
                           user=config.devices_db_user,
                           passwd=config.devices_db_passwd,
                           db=config.devices_db,
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def getWorkIssueConn():
    conn = pymysql.connect(host=config.workissue_db_host,
                           port=int(config.workissue_db_port),
                           user=config.workissue_db_user,
                           passwd=config.workissue_db_passwd,
                           db=config.workissue_db,
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn
