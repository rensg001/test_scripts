import argparse
import os
import time
import logging
import subprocess
import threading

import ujson

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


def get_config():
    with open("config.json", mode="r", encoding="utf8") as config_file:
        config = config_file.read()
        config_dict = ujson.loads(config)

    return config_dict


def init_logger(path):
    """初始化日志记录器

    :param path: 日志路径
    :return:
        logger
    """

    file_handler = logging.FileHandler(
        filename=path,
        mode="a",
        encoding="utf8",
    )
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[file_handler])


class LogCleaner(threading.Thread):
    """日志清洁工"""

    def __init__(self):
        super(LogCleaner, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def is_stoped(self):
        return self._stop_event.is_set()

    def run(self):
        while True:
            time.sleep(1)

            if self.is_stoped():
                break

            if os.path.exists(config["log_path"]) and os.path.getsize(
                    config["log_path"]) > (
                                1024 * 1024 * 1024 * config["log_size"]):
                os.remove(config["log_path"])


class PathParser(object):
    def __init__(self, path):
        self._path = path

    @property
    def extend(self):
        root, ext = os.path.splitext(self._path)
        return ext

    @property
    def path(self):
        return self._path

    @property
    def filename(self):
        return os.path.split(self._path)[-1]


class FileCreationEventHandler(FileSystemEventHandler):

    @staticmethod
    def move(path_parser):
        dest_path = config["destination"].get(path_parser.extend)
        if not dest_path:
            logging.info(
                "No destination for {path}".format(path=path_parser.path)
            )
            return

        if os.path.exists(os.path.join(dest_path, path_parser.filename)):
            logging.info(
                "The destination have a file with same name. "
                "{filename}".format(filename=path_parser.filename)
            )
            return

        subprocess.call(["mv", path_parser.path, dest_path])

    def on_created(self, event):
        self.move(PathParser(event.src_path))

    def on_moved(self, event):
        if event.dest_path.startswith(watch_path):
            self.move(PathParser(event.dest_path))


class MyLoggingEventHandler(LoggingEventHandler, FileCreationEventHandler):
    pass


config = get_config()

watch_path = ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="file path.", action="store")
    args = parser.parse_args()
    init_logger(config["log_path"])
    global watch_path
    watch_path = args.path

    log_handler = MyLoggingEventHandler()
    # file_creation_handler = FileCreationEventHandler()
    observer = Observer()
    observer.schedule(log_handler, args.path)
    # observer.schedule(file_creation_handler, args.path)
    observer.start()

    log_cleaner = LogCleaner()
    log_cleaner.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log_cleaner.stop()

    observer.join()
    log_cleaner.join()


if __name__ == "__main__":
    main()
