import logging


def get_logger():
    logger=logging.getLogger(__name__)
    #user define object from getLogger----
    handler=logging.FileHandler(r"/Users/nehakumari/PycharmProjects/FrameworkMyShop/Utils/logfile.log")
    formatting=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatting) #setting the format of log file

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.debug("a debug statement is executed")
    logger.info("a info statement ")
    logger.warning("warning mgs")
    logger.error("error is here")
    logger.critical("everything is over")
    return logger

