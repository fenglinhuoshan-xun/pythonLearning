"""
    1. 创建字符串：人生苦短，我用python
    2. 打印第一个字符，最后一个字符
    3. 打印前两个字符，后六个字符
    4. 打印中间一个字符
    5. 倒序打印所有字符
"""

message = "人生苦短，我用python"
print(message[0])
print(message[-1])
print(message[:2])
print(message[-6:])
print(message[len(message) // 2])
print(message[::-1])
