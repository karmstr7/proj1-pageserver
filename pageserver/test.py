import config
import os
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


def find_credentials():
    path = config.config_file_args(["../credentials.ini"])
    path = path["DOCROOT"]
    return path


def test_path():
    """
        Opens the requested file (html or css) and reads the file line by line.
        :param file_name: Name of the requested file.
        :return: The entire requested file in string.
        """
    source_path = os.path.join(find_credentials(), "trivia.html")
    print(source_path)

    response_body = """"""
    try:
        with open(source_path, 'r', encoding='utf-8') as source:
            for line in source:
                response_body = response_body + line
    except OSError as error:
        log.warn("Failed to open or read file")
        log.warn("Requested file was {}".format(source_path))
        log.warn("Exception: {}".format(error))

    return response_body
if __name__ == "__main__":
    test_path()
