from docker.models.containers import Container
from src.database.connection import DBConnection


def get_stats(container: Container, is_only_running: bool):
    db_connection = DBConnection()
    db = db_connection.get_database()
    collection = db['container_stats']

    filter = {
        '$or': [
            {'id': container.short_id},
            {'name': container.name}
        ]
    }

    if is_only_running:
        filter['status'] = 'running'

    stats = []

    for stats_aux in collection.find(filter=filter):
        del stats_aux['_id']
        stats.append(stats_aux)

    return stats
