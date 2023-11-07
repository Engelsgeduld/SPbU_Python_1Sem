from io import StringIO

from src.Homeworks.homework_5.task_1.utf_16 import *
import pytest


@pytest.mark.parametrize(
    "line, chars",
    (
        ("qwer", ["q", "w", "e", "r"]),
        ("1223", ["1", "2", "2", "3"]),
        ("äölöä", ["ä", "ö", "l", "ö", "ä"]),
        ("푸풍풅", ["푸", "풍", "풅"]),
    ),
)
def test_char_function(line, chars):
    actual = get_chars(line)
    assert actual == chars


@pytest.mark.parametrize(
    "chars,unicode",
    (
        (["Ā", "Ă", "Ą"], ["U+0100", "U+0102", "U+0104"]),
        (["푸", "풍", "풅"], ["U+D478", "U+D48D", "U+D485"]),
        (["𝆺𝅥𝅯", "𝇑", "𝇜"], ["U+1D1C0", "U+1D1D1", "U+1D1DC"]),
    ),
)
def test_get_unicode(chars, unicode):
    actual = get_unicode(chars)
    assert actual == unicode


@pytest.mark.parametrize(
    "chars, binary",
    (
        (("a", "b"), ["00000000 01100001", "00000000 01100010"]),
        (
            ("𝀂", "𝀋"),
            [
                "11011000 00110100 11011100 00000010",
                "11011000 00110100 11011100 00001011",
            ],
        ),
        (
            ("𝌠", "𝌬"),
            [
                "11011000 00110100 11011111 00100000",
                "11011000 00110100 11011111 00101100",
            ],
        ),
    ),
)
def test_binary_utf(chars, binary):
    print(chars, binary)
    actual = get_utf_16(chars)
    assert actual == binary


def test_main_scenario(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "ar𫝆")
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert (
        output
        == "UTF-16 encoding:\na    U+0061    00000000 01100001\nr    U+0072    00000000 01110010\n𫝆    U+2B746   11011000 01101101 11011111 01000110\n"
    )
