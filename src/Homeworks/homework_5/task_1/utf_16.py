import re


def get_unicode(char):
    codepoint = hex(ord(char))[2:]
    unicode_sign = "U+"
    zero_line = "0" * (4 - len(codepoint))
    unicode_code_line = (unicode_sign + zero_line + codepoint).upper()
    return unicode_code_line


def height_lows_bytes(char):
    if char > 0x10000:
        char = char - 0x10000
        height_part = bin(char // 0x400 + 0xD800)[2:]
        low_part = bin(char % 0x400 + 0xDC00)[2:]
        return height_part + low_part
    else:
        char_binary = bin(char)[2:]
        zero_line = "0" * (16 - len(char_binary))
        return zero_line + char_binary


def get_utf_16(char):
    codepoint = int(hex(ord(char)), 16)
    utf_code = height_lows_bytes(codepoint)
    return utf_code


def format_utf_16(utf_16):
    formatted_utf_codes = list(
        map(lambda x: " ".join(re.findall(f'{"."*8}', x)), utf_16)
    )
    return formatted_utf_codes


def print_line(string):
    print("UTF-16 encoding:")
    for i in string:
        print("{:<5}{:<10}{}".format(*i))


def main():
    user_line = input("Enter a string:")
    chars = list(user_line)
    unicodes = list(map(get_unicode, chars))
    utf = list(map(get_utf_16, chars))
    formatted_utf = format_utf_16(utf)
    strings = zip(chars, unicodes, formatted_utf)
    print_line(strings)


if __name__ == "__main__":
    main()
