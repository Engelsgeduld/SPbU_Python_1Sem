from io import StringIO

from src.Homeworks.homework_5.task_2.dna_compress import *
import pytest
import random
import string


@pytest.mark.parametrize(
    "line, expected", (("abcdefg", "a1b1c1d1e1f1g1"), ("aaaabbсaa", "a4b2с1a2"))
)
def test_compress_function(line, expected):
    actual = compress_line(line)
    assert actual == expected


@pytest.mark.parametrize(
    "line, expected", (("a1d1c1f1", "adcf"), ("i4o1i1o1", "iiiioio"))
)
def test_decode_function(line, expected):
    actual = decode_line(line)
    assert actual == expected


@pytest.mark.parametrize(
    "value",
    (("".join(random.choices(string.ascii_letters, k=100000))) for _ in range(10)),
)
def test_compress_decode_chain(value):
    actual = decode_line(compress_line(value))
    assert actual == value


@pytest.mark.parametrize(
    "input_line",
    ("3aaa2", "я3к5з6", "a\n334", "a**76$", "a*5", "äößßß", "ac345", "", "a4c"),
)
def test_compress_line_validation_exception(input_line):
    with pytest.raises(ValueError):
        validate_compress_input(input_line)


def test_compress_line_validation_normal_scenario():
    actual = validate_compress_input("a3b4c56")
    assert actual == "a3b4c56"


@pytest.mark.parametrize(
    "input_line",
    (
        " ",
        "123",
        "aaa3456",
        "kkkЯРУССКИЙlll",
        "einpaarwörteraufDeutschmitumlaut",
        "<>/oppp",
        "A lot of space",
        "o\np",
        "\\u3232",
        "\u3232",
        "",
    ),
)
def test_line_validation_exceptions(input_line):
    with pytest.raises(ValueError):
        validate_user_dna_input(input_line)


@pytest.mark.parametrize(
    "input_line", ("wortaberohneumlaut", "aaaper", "ApErTy", "qwertyuiop", "qwertz")
)
def test_line_validation_normal_scenario(input_line):
    actual = validate_user_dna_input(input_line)
    assert actual == input_line


@pytest.mark.parametrize(
    "inputs, unique_output",
    (
        (("1", "45698"), "Only latin letters allowed"),
        (("1", ""), "Got an empty line"),
        (("1", "abfccc"), "Compress DNA:a1b1f1c3"),
        (("2", "4abc"), "Compressed line must begin with latin letter"),
        (("2", "a4c*5"), "Only latin letters and digits allowed"),
        (("2", "abc456"), "Compress Error 2 letters near by"),
    ),
)
def test_main_scenario(monkeypatch, inputs, unique_output):
    fake_output = StringIO()
    responses = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == unique_output + "\n"
