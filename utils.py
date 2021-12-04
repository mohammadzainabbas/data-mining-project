import re


def extract_integer(alpha_numeric_str: str):
    try:
        int_part = re.sub(r'[^\d]', '', alpha_numeric_str)
        numeric = int(int_part)
    except ValueError as ve:
        print(f"ValueError: {ve}")
        numeric = None
    return numeric


if __name__ == '__main__':
    assert 245 == extract_integer("hlk245.sdf")
