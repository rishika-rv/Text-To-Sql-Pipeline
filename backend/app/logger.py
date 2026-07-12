import logging

logging.basicConfig(
    filename="text_to_sql.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)