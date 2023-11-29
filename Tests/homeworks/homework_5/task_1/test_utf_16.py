from io import StringIO

from src.Homeworks.homework_5.task_1.utf_16 import *
import pytest


@pytest.mark.parametrize(
    "chars,unicode",
    (
        ("Ā", "U+0100"),
        ("Ă", "U+0102"),
        ("Ą", "U+0104"),
        ("푸", "U+D478"),
        ("풍", "U+D48D"),
        ("풅", "U+D485"),
        ("𝆺𝅥𝅯", "U+1D1C0"),
        ("𝇑", "U+1D1D1"),
        ("𝇜", "U+1D1DC"),
    ),
)
def test_get_unicode(chars, unicode):
    actual = get_unicode(chars)
    assert actual == unicode


@pytest.mark.parametrize(
    "chars, binary",
    (
        ("a", "0000000001100001"),
        ("b", "0000000001100010"),
        ("𝀂", "11011000001101001101110000000010"),
        ("𝀋", "11011000001101001101110000001011"),
        ("𝌠", "11011000001101001101111100100000"),
        ("𝌬", "11011000001101001101111100101100"),
    ),
)
def test_binary_utf(chars, binary):
    actual = get_utf_16(chars)
    assert actual == binary


@pytest.mark.parametrize(
    "utf, formatted_utf",
    (
        (["0000000001100001"], ["00000000 01100001"]),
        (["11011000001101001101110000000010"], ["11011000 00110100 11011100 00000010"]),
    ),
)
def test_format_utf(utf, formatted_utf):
    actual = format_utf_16(utf)
    assert actual == formatted_utf


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
