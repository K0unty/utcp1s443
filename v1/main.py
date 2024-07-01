#!/usr/bin/env python3 

# Prettify 
# Prettifyer code

# ------------------------------------------------------
import mod1
# ------------------------------------------------------

# ------------------------------------------------------
from rich import print as rprint # For rprinting
from rich.pretty import pprint # For pretty printing
from rich import inspect # For inspect
from rich.console import Console # For console.print
from rich.markdown import Markdown # For markdown
from rich.panel import Panel # For Panel()
from rich import box # For Panel Boxes
from rich.prompt import Prompt # For Prompting 
console = Console() # Standard code to access console
# -------------------------------------------------------

rprint(f'''
[bright_cyan]Hello World![/bright_cyan]      
''')

rprint(mod1.pi)
