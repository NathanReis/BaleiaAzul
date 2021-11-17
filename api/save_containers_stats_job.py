from datetime import datetime
from src.database.connection import DBConnection
from src.helpers.docker_helper import extract_stats_container_data
from src.services import container_service
import schedule
import time


def save_containers_stats():
    db_connection = DBConnection()
    db = db_connection.get_database()
    containers = container_service.get_all()

    for container in containers:
        stats = container_service.get_stats(container, True, False)
        stats_data = extract_stats_container_data(container, stats)

        db['container_stats'].insert_one(stats_data)

    print(datetime.utcnow())


time_to_wait = 10

schedule.every(time_to_wait).seconds.do(save_containers_stats)

while True:
    schedule.run_pending()
    time.sleep(time_to_wait)
