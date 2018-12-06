from psutil import virtual_memory

def total_memory():
    '''
    total_memory returns total memory
    on local machine
    '''
    return virtual_memory().total


class PgConfWizard:
    def __init__(self, path):
        self.path = path
        self.config = {}
    
    def read_file(self):
        '''
            read_file provides reading of the postgres.conf
            file an parsing of config
        '''
        for i, line in enumerate(open(self.filename)):
            splitter = line.split('\n')
            if len(splitter) == 0:
                continue
            line = splitter[0]
            # if line is comment, then go to the next one
            if line[0] == '#':
                continue
            splitter_line = line.split('=')
            # optionally line might not contains '='
            if len(splitter_line) == 1:
                splitter_line = line.split(' ')
            self.config[splitter_line[0]] = splitter_line[1]

