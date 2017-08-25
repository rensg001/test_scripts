#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os
import ujson
import logging
import argparse
import subprocess


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

    logger = logging.getLogger("file_dispatcher")
    logger.setLevel(level=logging.INFO)
    file_handler = logging.FileHandler(filename=path, mode="a",
                                       encoding="utf8")
    logger.addHandler(file_handler)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    return logger


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="file path.", action="store")
    args = parser.parse_args()
    config = get_config()
    logger = init_logger(config["log_path"])

    if not os.path.exists(args.path):
        # logger.info("file path {path} does not exists.".format(path=args.path))
        exit(0)

    path_parser = PathParser(args.path)
    dest_path = config["destination"].get(path_parser.extend)
    if not dest_path:
        logger.info(
            "There is no destination for {path}".format(path=path_parser.path))
        exit(0)

    if os.path.exists(os.path.join(dest_path, path_parser.filename)):
        logger.info("The destination have same name file. {filename}".format(
            filename=path_parser.filename))
        exit(0)

    subprocess.call(["mv", path_parser.path, dest_path])
    logger.info("Moved {origin} to {dest}".format(origin=path_parser.path,
                                                  dest=dest_path))
