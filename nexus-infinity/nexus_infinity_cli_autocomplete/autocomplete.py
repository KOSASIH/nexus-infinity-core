import os
import readline
import fuzzywuzzy
from fuzzywuzzy import process
from completion_engine import CompletionEngine
from cli_commands import CLI_COMMANDS
from config import AUTOCOMPLETE_ENABLED, FUZZY_MATCHING_ENABLED

class Autocomplete:
    def __init__(self, cli_commands):
        self.cli_commands = cli_commands
        self.completion_engine = CompletionEngine()
        self.fuzzy_matcher = FuzzyMatcher()

    def enable_autocomplete(self):
        readline.set_completer(self.complete)
        readline.parse_and_bind("tab: complete")

    def complete(self, text, state):
        if FUZZY_MATCHING_ENABLED:
            return self.fuzzy_matcher.complete(text, state, self.cli_commands)
        else:
            return self.completion_engine.complete(text, state, self.cli_commands)

    def disable_autocomplete(self):
        readline.set_completer(None)

class FuzzyMatcher:
    def __init__(self):
        self.cache = {}

    def complete(self, text, state, cli_commands):
        # Tokenize the input text
        tokens = text.split()

        # Find the current command and its options
        current_command = None
        for command in cli_commands:
            if tokens[0] == command["command"]:
                current_command = command
                break

        # Generate completion options using fuzzy matching
        options = []
        if current_command:
            for option in current_command["options"]:
                if option.startswith(tokens[-1]):
                    options.append(option)
                else:
                    ratio = process.ratio(option, tokens[-1])
                    if ratio > 60:  # Adjust the fuzzy matching threshold as needed
                        options.append(option)

        # Return the completion options
        return options[state]

class CommandHistory:
    def __init__(self):
        self.history = []

    def add_command(self, command):
        self.history.append(command)

    def get_suggestions(self, text):
        suggestions = []
        for command in self.history:
            if command.startswith(text):
                suggestions.append(command)
        return suggestions

class DynamicOptionGenerator:
    def __init__(self):
        self.generators = {}

    def add_generator(self, command, generator):
        self.generators[command] = generator

    def generate_options(self, command, text):
        if command in self.generators:
            return self.generators[command](text)
        else:
            return []

def init_autocomplete(cli_commands):
    if AUTOCOMPLETE_ENABLED:
        autocomplete = Autocomplete(cli_commands)
        autocomplete.enable_autocomplete()

def load_cli_commands():
    return CLI_COMMANDS

def main():
    cli_commands = load_cli_commands()
    init_autocomplete(cli_commands)

if __name__ == "__main__":
    main()
