import textwrap

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from src.decorators import input_error, interrupt_error

def wrap_text(text, width, initial_indent, subsequent_indent):
    return textwrap.fill(text, width=width,
                         initial_indent=initial_indent,
                         subsequent_indent=subsequent_indent)


@interrupt_error
@input_error
def parse_input(cmd_list:list[str], session:PromptSession):
    cmd_completer = FuzzyWordCompleter(cmd_list, WORD=True)
    user_input = session.prompt("Enter a command: ",
                                completer=cmd_completer,
                                complete_style=CompleteStyle.MULTI_COLUMN,
                                reserve_space_for_menu=5,
                                auto_suggest=AutoSuggestFromHistory())
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
