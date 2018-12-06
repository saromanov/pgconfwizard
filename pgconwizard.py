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
        for i, line in enumerate(open(self.filename)):
            splitter = line.split('\n')
            if len(splitter) == 0:
                continue
            line = splitter[0]
            # if line is comment, then go to the next one
            if line[0] == '#':
                continue

