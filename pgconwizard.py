import platform
from psutil import virtual_memory

def total_memory():
    '''
    total_memory returns total memory
    on local machine
    '''
    return virtual_memory().total

def get_architecture():
    '''
    return 32 if app running on 32 bit arch
    or 64 if app running at 32 bit arch
    '''
    result = platform.architecture()
    if len(result) != 2:
        raise Exception("Unable to get platform.architecture")
    return result[0].split('bit')



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
            self.config[splitter_line[0].strip()] = splitter_line[1].strip()

    def attributes(self):
        '''
            attributes returns config map
        '''
        return self.config


class OptimialSettings:
    def __init__(self):
        pass
    
    def shared_buffers(self):
        '''
        In the simple case, shared buffers should be 1/4
        from total memory
        '''
        arch = get_architecture()
        if arch is '32':
            available_memory = 3000000000
            return available_memory/1.5
        return total_memory / 4

