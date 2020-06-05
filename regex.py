import re

# Biên dịch 1 regex expression thành 1 regex expression object. Từ đó có thể dùng các hàm match(), search()
prog = re.compile(pattern)
result = prog.match(string)

result = re.match(pattern, string)
