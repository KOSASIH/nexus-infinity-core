import os
import readline
from config import get_config
from completion_engine import CompletionEngine

def init_autocomplete():
    """
    Initializes the autocompletion feature.
    """
    config = get_config()
    if not config.get_config("autocomplete", "enabled"):
        return

    # Set up readline for autocompletion
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)

    # Initialize the completion engine
    engine = CompletionEngine()

def complete(text, state):
    """
    Completes the input text using the completion engine.

    :param text: The input text to complete
    :param state: The completion state
    :return: The completed text
    """
    engine = CompletionEngine()
    options = engine.get_completion_options(text, text)
    if state < len(options):
        return options[state]
    else:
        return None

def main():
    init_autocomplete()

if __name__ == "__main__":
    main()
