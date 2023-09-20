import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="/home/mubashar4603/PycharmProjects/Metutors/Logs/automation.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

