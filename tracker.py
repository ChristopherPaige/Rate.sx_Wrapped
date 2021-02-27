import os

from custom_query import exe

def crypto_tracker(command, **kwargs):
    return command
    
crypto_tracker(os.system("curl rate.sx"))

exe(
    "curl rate.sx/eth", 
    "curl rate.sx/btc" , 
    "curl rate.sx/ada", 
    "curl rate.sx/link"
)
