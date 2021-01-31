# python-str-dict-to-json

Convert the string representation of a Python dict to JSON

## Example

You've got a Python dict that was printed to a log file. You want to run it through JSON tools, like [jq](https://stedolan.github.io/jq/) but it's not actually JSON.

```
{'example': {'number': 42, 'text': 'lorem ipsum', 'boolean': True}}
```

Let's convert it to JSON with:

```
$ cat input.txt | python3 main.py
{"example": {"number": 42, "text": "lorem ipsum", "boolean": true}}
```

We could even pipe it to `jq`:

```
$ cat input.txt | python3 main.py | jq .example.number
42
```
