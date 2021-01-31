import ast
import click
import json
import re
import sys

@click.command()
@click.option('--lines', required=False, is_flag=True)
@click.argument('input_file', required=False, type=click.File('r'))
def convert(input_file, lines):
    '''
    Convert from Python dict literal to JSON
    '''
    if not input_file:
        input_file = sys.stdin
    contents = input_file.read().strip()
    if not contents:
        return
    if lines:
        for line in re.split("[\r\n]{1,2}", contents):
            click.echo(convertToJson(line))
    else:
        click.echo(convertToJson(contents))


def convertToJson(text):
    d = ast.literal_eval(text)
    return json.dumps(d)

if __name__ == '__main__':
    convert()

