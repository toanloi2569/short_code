import re

partern = r'^[0-9a-z]{8}$'
string = 'ms201669'

# re.compile(pattern, flags=0)
# Biên dịch 1 regex expression thành 1 regex expression object. Từ đó có thể dùng các hàm match(), search()
prog = re.compile(pattern)
result = prog.match(string)


#re.finditer(pattern, string, flags=0)
# Trả về iterator match objects
matchs = re.finditer(pattern, string)
