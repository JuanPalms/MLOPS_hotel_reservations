import traceback
import sys

### We need custom and predefined exceptions also
class CustomException(Exception):

  def __init__(self, error_message, error_detail:sys):
    super().__init__(error_message)
    self.error_message = self.get_detailed_error_message(error_message, error_detail)
  
  @staticmethod
  def get_detailed_error_message(error_message, error_detail:sys):

    _,_, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # Give you the filename where the error occurs
    line_number = exc_tb.tb_lineno #Give you the line number where the error occurs

    return f"Error in {file_name}, line {line_number}: {error_message}"
  
  def __str__(self): #gives a text representation of the error message
    return self.error_message


