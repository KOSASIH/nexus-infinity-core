import os
import json

# Load CLI commands from a JSON file
with open('cli_commands.json', 'r') as f:
    CLI_COMMANDS = json.load(f)

# Define a dictionary to store dynamic command options
DYNAMIC_OPTIONS = {}

def add_dynamic_option(command, generator):
    DYNAMIC_OPTIONS[command] = generator

def get_dynamic_options(command, text):
    if command in DYNAMIC_OPTIONS:
        return DYNAMIC_OPTIONS[command](text)
    else:
        return []

# Define CLI commands with their corresponding completion options
CLI_COMMANDS = [
    {
        "command": "nexus",
        "options": ["--help", "--version", "init", "create", "delete"],
        "description": "Nexus Infinity CLI"
    },
    {
        "command": "nexus init",
        "options": ["--template", "--name", "--description"],
        "description": "Initialize a new Nexus Infinity project"
    },
    {
        "command": "nexus create",
        "options": ["--type", "--name", "--description"],
        "description": "Create a new resource in Nexus Infinity"
    },
    {
        "command": "nexus delete",
        "options": ["--name", "--force"],
        "description": "Delete a resource in Nexus Infinity"
    },
    {
        "command": "nexus config",
        "options": ["--get", "--set", "--list"],
        "description": "Manage Nexus Infinity configuration"
    },
    {
        "command": "nexus plugin",
        "options": ["--install", "--uninstall", "--list"],
        "description": "Manage Nexus Infinity plugins"
    }
]

# Add dynamic options for the 'nexus create' command
def create_resource_options(text):
    resources = ["vm", "container", "database"]
    return [resource for resource in resources if resource.startswith(text)]

add_dynamic_option("nexus create", create_resource_options)

# Add dynamic options for the 'nexus plugin' command
def plugin_options(text):
    plugins = ["plugin1", "plugin2", "plugin3"]
    return [plugin for plugin in plugins if plugin.startswith(text)]

add_dynamic_option("nexus plugin", plugin_options)
