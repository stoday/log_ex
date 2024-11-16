
import log_ex

log_ex.log(message='This is a start message', type='INFO', verbose=True)

# try:
#     1/0
# except ZeroDivisionError:
#     log_ex.log(message='This is a error message', 
#                type='ERROR', 
#                verbose=False,
#                logfile_by_day=False)

log_ex.log(message='This is a end message', type='INFO', verbose=True)
