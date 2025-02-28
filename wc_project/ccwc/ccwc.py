"""This module provides the wc CLI."""
# ccwc.py
from click.exceptions import BadArgumentUsage
from ccwc import __app_name__, __version__
from typing import Optional, Tuple, Union
from typing_extensions import Annotated
from pathlib import Path
import typer
import os
import sys


# create the app
app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value: 
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit


def get_file_size(file_name: Path) -> int:

    return os.path.getsize(file_name) 


def get_file_lines(file_name: Path) -> int:

    with open(file_name, 'r') as f:
        num_lines = sum(1 for _ in f) 

    return num_lines


def get_all_stats(file_name: Path) -> Tuple:

    return get_file_lines(file_name), get_file_size(file_name)


def get_piped_lines() -> int:
    """Returns the number of lines from piped input."""
    return sum(1 for _ in sys.stdin)


# Typer is smart enough to create a CLI application with that single function as the main CLI application, not as a command/subcommand:
@app.command()
def main(
    # the only CLI option for the main CLI
    file_name: Annotated[Optional[Path], typer.Argument()] = None,
    version: Annotated[bool, typer.Option(
        "--version",
        "-v",
        help="Show app's version and exit",
        callback=_version_callback, #attaches this callback to invocation of version option
        is_eager=True #Processes this before all else
        )] = False,
    file_size: Annotated[bool, typer.Option(
        "--file-size",
        "-c",
        is_flag=True,
        help="Return size of file in bytes",
        )] = False,
    file_lines: Annotated[bool, typer.Option(
        "--file-lines",
        "-l",
        help="Return lines in file in bytes",
        )] = False,
    ) -> None:

    is_piped = not sys.stdin.isatty()

    if not is_piped:
        if file_name is None:
            raise BadArgumentUsage("Missing argument 'FILE_NAME'.")
        
        if not (file_size or file_lines):
            lines, size = get_all_stats(file_name)
            typer.echo(f"\t{lines}  {size}  {file_name}")
            raise typer.Exit()

    if file_size:
        size = get_file_size(file_name)
        typer.echo(f"\t{size}  {file_name}")
        raise typer.Exit()

    if file_lines:
        if is_piped:
            lines = get_piped_lines()
            typer.echo(f"\t{lines}")
        else:
            lines = get_file_lines(file_name)
            typer.echo(f"\t{lines}  {file_name}")
        
        raise typer.Exit()


    return

