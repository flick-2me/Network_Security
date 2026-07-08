import sys
from networksecurity.logging.logger import logging


class NetworkSecurityException(Exception) : 
    def __init__(self,error,error_details:sys):
        super().__init__(error)
        _,_,exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_no = exc_tb.tb_lineno
        self.error_message = error
        logging.error(f"error {self.error_message} ")
    def __str__(self) :
        return "Error occured in lienno [{0}] in file [{1}] with error message : [{2}]".format(self.line_no,self.file_name,self.error_message)
    



