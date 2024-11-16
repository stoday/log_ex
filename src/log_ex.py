
import logging
import datetime as dt
import traceback
import pdb


def log(message: str = '', 
        type: str = 'INFO', 
        verbose: bool = True, 
        logfile_by_day: bool = False) -> None:
    """_description_
    Simple logging function to log messages to the screen or to a file.

    Parameters
    ----------
    message : str, optional
        logging message, by default ''
    type : str, optional
        there are three types: ERROR, WARNING, INFO, by default 'INFO'
    verbose : str, optional
        show the messages in the screen, by default True
    logfile_by_day : bool, optional
        name of logfile is built by date, log-xxxxxxxx, by default False

    Returns
    -------
    _type_
        _description_
    """

    
    # 設置 logging 寫入檔案
    logging.basicConfig(level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='log.log',
                        filemode='a')
    
    # 設置 logging 寫入螢幕
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s -  - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    
    if type == 'INFO':
        logging.info(message)
        
    elif type == 'WARNING':
        logging.warning(message)
        
    elif type == 'ERROR':
        logging.error(message + '\n\n-------\n' + traceback.format_exc() + '-------\n')
    
    # log_file = 'log.log'
    # file_handler = logging.FileHandler(log_file)
    # file_formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    # file_handler.setFormatter(file_formatter)
    # file_logger = logging.getLogger()
    # file_logger.addHandler(file_handler)
    # file_logger.removeHandler(logging.StreamHandler())
    
    # if type == 'INFO':
    #     file_logger.info(message)
        
    # elif type == 'WARNING':
    #     file_logger.warning(message)
        
    # elif type == 'ERROR':
    #     file_logger.error(message + '\n\n-------\n' + traceback.format_exc() + '-------\n')
            
    # if verbose:
    #     if type == 'INFO':
    #         logging.info(message)
            
    #     elif type == 'WARNING':
    #         logging.warning(message)
            
    #     elif type == 'ERROR':
    #         logging.error(message)
        
    return None


        
