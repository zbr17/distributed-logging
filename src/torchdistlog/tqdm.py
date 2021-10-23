from tqdm import tqdm as tqdm_ori
import torch.distributed as dist

class TqdmWithoutPrint:
    def __init__(self, iterable):
        self.iterable = iterable
    
    def __iter__(self):
        for item in iter(self.iterable):
            yield item

def tqdm(iterable):
    if dist.is_initialized():
        if dist.get_rank() == 0:
            return tqdm_ori(iterable)
        else:
            return TqdmWithoutPrint(iterable)
    else:
        return tqdm_ori(iterable)
    
