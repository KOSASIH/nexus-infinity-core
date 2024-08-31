import os
import re
from cli_commands import CLI_COMMANDS, get_dynamic_options

class CompletionEngine:
    def __init__(self):
        self.cli_commands = CLI_COMMANDS

    def get_completion_options(self, command, text):
        """
        Returns a list of completion options for the given command and input text.

        :param command: The current command being typed
        :param text: The input text to generate completion options for
        :return: A list of completion options
        """
        options = []
        for cmd in self.cli_commands:
            if cmd["command"].startswith(command):
                options.extend(self.get_options(cmd, text))
        return options

    def get_options(self, cmd, text):
        """
        Returns a list of completion options for the given command and input text.

        :param cmd: The command object
        :param text: The input text to generate completion options for
        :return: A list of completion options
        """
        options = []
        if "options" in cmd:
            options.extend(self.filter_options(cmd["options"], text))
        if cmd["command"] in get_dynamic_options:
            options.extend(get_dynamic_options(cmd["command"], text))
        return options

    def filter_options(self, options, text):
        """
        Filters the given options based on the input text.

        :param options: The list of options to filter
        :param text: The input text to filter options for
        :return: A list of filtered options
        """
        return [option for option in options if option.startswith(text)]

    def get_command_description(self, command):
        """
        Returns the description for the given command.

        :param command: The command to get the description for
        :return: The command description
        """
        for cmd in self.cli_commands:
            if cmd["command"] == command:
                return cmd["description"]
        return ""

def main():
    engine = CompletionEngine()
    # Example usage:
    command = "nexus create"
    text = "vm"
    options = engine.get_completion_options(command, text)
    print(options)  # Output: ["vm"]

if __name__ == "__main__":
    main()
