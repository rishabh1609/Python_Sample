import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler
class TestLogging:
    def __init__(self, path, jobid=1000):
        date = time.strftime("%Y_%m_%d")
        logger_path = str(path + "/logs/Test_" + str(date) + "_" + str(jobid) + ".log")
        fh = logging.FileHandler(logger_path)
        self.logger = logging.getLogger("Test" + str(jobid))
        if len(self.logger.handlers) > 0:
            pass
        else:
            self.logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(funcName)2s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

if __name__=="__main__":
    a=TestLogging("")
