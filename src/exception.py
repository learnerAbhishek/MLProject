import sys
import logging


def error_message(error, error_det : sys):
    _,_,exc_tb = error_det.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occurred in python script [{0}] line number [{1}] \
        error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_msg 

class CustomException(Exception):
    def __init__(self,error_msg,error_det):
        super().__init__(error_msg)
        self.error_msg = error_message(error_msg,error_det=error_det)

    def __str__(self) -> str:
        return self.error_msg     
