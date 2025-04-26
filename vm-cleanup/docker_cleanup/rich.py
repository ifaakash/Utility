from main import Table
from main import console

# Rich package to show output in CLI friendly way
def rich_output(title, col1, col2, row1col1, row2col1, row1col2, row2col2):
    table = Table(title=f"{title}")
    table.add_column(f"{col1}", style="cyan")
    table.add_column(f"{col2}", style="magenta")

    table.add_row(f"{row1col1}", f"{row1col2}")
    table.add_row(f"{row2col1}", f"{row2col2}")

    console.print(table)
