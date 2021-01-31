from pydict2json import convert
import pathlib

HERE = pathlib.Path(__file__).parent

def test_primitives():
    assert convert('{}') == '{}'
    assert convert('[]') == '[]'

def test_dicts():
    a = {'a': 'A', 'b': 42, 'c': 0.0, 'd': False, 'e': None}
    assert convert(str(a)) == '{"a": "A", "b": 42, "c": 0.0, "d": false, "e": null}'

def test_arrays():
    a = [1,2,3,"a",False,None]
    assert convert(str(a)) == '[1, 2, 3, "a", false, null]'

def test_file():
    with (HERE / "input.txt").open() as f:
        a = convert(input_file=f)
    assert a == '{"example": {"number": 42, "text": "lorem ipsum", "boolean": true}}'

def test_lines_file():
    with (HERE / "lines.txt").open() as f:
        a = convert(input_file=f, lines=True)
    a = [ _ for _ in a ]
    assert len(a) == 5
    assert a[0] == '{"a": 42}'
    assert a[1] == '{"b": 43}'
    assert a[2] == '{"c": 44}'
    assert a[3] == '{"d": 45}'
    assert a[4] == '{"e": 46}'

def test_pretty():
    a = convert("{'a': 1, 'b': {'c': 'd'}}", pretty=True)
    assert a == '{\n  "a": 1,\n  "b": {\n    "c": "d"\n  }\n}'

