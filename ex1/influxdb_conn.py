import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "webscrapping"
url = "http://localhost:8086"
bucket="webscrapping"


def send_data(points):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        version = client.version()
        # print(f"InfluxDB: {version}")
        write_api = client.write_api(write_options=SYNCHRONOUS)
        successfully = write_api.write(bucket=bucket, record=points)
        print(f" > successfully: {successfully}")
 


