# pylint: disable=logging-fstring-interpolation
import logging
from datetime import datetime

from shhh.extensions import scheduler
from shhh.models import Entries

logger = logging.getLogger("tasks")


def delete_expired_links():
    """Delete expired links from the database."""
    app = scheduler.app
    with app.app_context():
        expired = Entries.query.filter(Entries.date_expires <= datetime.now()).all()
        for record in expired:
            record.delete()
        logger.info(f"{len(expired)} expired records have been deleted.")
