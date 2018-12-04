from psutil import virtual_memory

def total_memory():
    '''
    total_memory returns total memory
    on local machine
    '''
    return virtual_memory().total
