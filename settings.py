# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

f = logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(f)
logger.addHandler(ch)
