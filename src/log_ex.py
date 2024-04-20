
import logging
import datetime as dt
import traceback


def log(content: str = '', 
        level: str = 'INFO', 
        log_output: str = 'screen', 
        logfile_by_day: bool = False) -> None:
    """
    Log the content with the specified level.
    """
    
    if log_output == 'screen':
        logging.basicConfig(level=logging.DEBUG, 
                            format='[%(asctime)s] %(levelname)s - %(message)s')

        if level == 'INFO':
            logging.info(content)
            
        elif level == 'WARNING':
            logging.warning(content)
            
        elif level == 'ERROR':
            logging.error(content)

        
    if log_output == 'file':
        if logfile_by_day:
            log_file = dt.datetime.now().strftime('%Y-%m-%d') + '.log'
        else:
            log_file = 'log.log'
        
        logging.basicConfig(level=logging.INFO,
                            format='[%(asctime)s] %(levelname)s - %(message)s',
                            filename=log_file,
                            filemode='a')

        if level == 'INFO':
            logging.info(content)
            
        elif level == 'WARNING':
            logging.warning(content)
            
        elif level == 'ERROR':
            logging.error(content)
            
    return None

        
