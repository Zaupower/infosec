import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "p_WiwHSFIOAI9U461JolHwMXfEDRzwbYOamZ3rOPnqGy0AhXFxZIeU8I5vSxQB1iZRBQLrS9eRiMdh8QuuPfPQ=="
org = "webscrapping"
url = "http://localhost:8086"
bucket="webscrapping2"


def send_data(points):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        version = client.version()
        # print(f"InfluxDB: {version}")
        write_api = client.write_api(write_options=SYNCHRONOUS)
        successfully = write_api.write(bucket=bucket, record=points)
        print(f" > successfully: {successfully}")
 


