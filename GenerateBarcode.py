from barcode import EAN13
from barcode.writer import ImageWriter
num : '5901234123457'
my_code = EAN13(num, writer=ImageWriter())
my_code.save("new_code")