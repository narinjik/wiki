import wikipedia
from loguru import logger
from wikipedia_project.processing import get_content


def main():
    try:
        res = get_content()
        logger.info(f"get content for preferred keyword {res}")
    except (IndexError, wikipedia.exceptions.PageError) as err:
        logger.info(f"error ka {err}")


if __name__ == "__main__":
    main()
