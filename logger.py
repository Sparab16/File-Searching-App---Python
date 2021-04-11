import logging as log

# Setting the log file
log.basicConfig(filename='file_search.log', level=log.WARNING,
                format= '\n[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')
