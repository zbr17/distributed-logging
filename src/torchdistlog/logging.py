import logging
import torch.distributed as dist

INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
FATAL = logging.FATAL
CRITICAL = logging.CRITICAL

class Indicator(object):
    def __init__(self, is_dist=False, output_rank=0):
        self.is_dist = is_dist
        self.output_rank = output_rank
    
indicator = Indicator()

def set_dist(is_dist=False):
    indicator.is_dist = is_dist
    if is_dist:
        logging.info("Set logger to DISTRIBUTED mode!")

def info(msg, *args, **kwargs):
    if indicator.is_dist:
        rank = dist.get_rank()
        if rank == indicator.output_rank:
            logging.info(msg, *args, **kwargs)
    else:
        logging.info(msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    if indicator.is_dist:
        rank = dist.get_rank()
        if rank == indicator.output_rank:
            logging.warning(msg, *args, **kwargs)
    else:
        logging.warning(msg, *args, **kwargs)

getLogger = logging.getLogger

if __name__ == "__main__":
    warning("test")