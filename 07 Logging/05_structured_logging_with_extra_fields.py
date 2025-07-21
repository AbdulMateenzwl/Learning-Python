import logging

logger = logging.getLogger("myLogger")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(user)s - %(message)s"
)

extra = {'user': 'abdul'}

logger.warning("Something happened", extra=extra)
