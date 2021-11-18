from .commands import cmd as cmd_commands
from .quit import cmd as cmd_quit
from .about import cmd as cmd_about
from .look_around import cmd as cmd_look_around
from .inventory import cmd as cmd_inventory
from .drop import cmd as cmd_drop
from .take import cmd as cmd_take
from .examine import cmd as cmd_examine

commands = [
    cmd_commands,
    cmd_quit,
    cmd_about,
    cmd_look_around,
    cmd_inventory,
    cmd_take,
    cmd_drop,
    cmd_examine
]
