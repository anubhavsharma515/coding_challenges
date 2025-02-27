"""This module provides the wc CLI."""
# ccwc.py

from wc import __app_name__, __version__
from typing import Optional
import typer


# create the app
app = typer.Typer()

def _version_callback(value: bool = True) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit


# When you create an app = typer.Typer() it works as a group of commands.
# And you can create multiple commands with it.
# Each of those commands can have their own CLI parameters.
# But as those CLI parameters are handled by each of those commands, 
# they don't allow us to create CLI parameters for the main CLI application itself.
# app.callback does this. It also specifying parameters for the main CLI, not the CLI's
# commands
@app.callback()
def main(
    # the only CLI option for the main CLI
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show app's version and exit",
        callback=_version_callback, #attaches this callback to invocation of version option
        is_eager=True
        )
    ) -> None:

    return
