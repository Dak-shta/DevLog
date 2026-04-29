import click
import requests

from rich.console import Console
from rich.table import Table
from rich import print

console = Console()


API_URL = "http://127.0.0.1:9000"

@click.group()
def cli():
    pass

# ADD LOG
def display_logs(logs):
    if not logs:
        console.print("[bold red]No logs found![/bold red]")
        return

    table = Table(title="📘 Dev Logs")

    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Yesterday", style="green")
    table.add_column("Today", style="yellow")
    table.add_column("Blockers", style="red")

    for log in logs:
        table.add_row(
            str(log["id"]),
            log["yesterday"],
            log["today"],
            log["blockers"] or "None"
        )

    console.print(table)
@cli.command()
@click.option("--yesterday", prompt="Yesterday")
@click.option("--today", prompt="Today")
@click.option("--blockers", default="", prompt="Blockers")
def log(yesterday, today, blockers):
    res = requests.post(
        f"{API_URL}/logs",
        params={
            "yesterday": yesterday,
            "today": today,
            "blockers": blockers
        }
    )
    print(res.json())

# GET ALL LOGS
@cli.command()
def list():
    res = requests.get(f"{API_URL}/logs")
    logs=res.json()
    display_logs(logs)
# GET WEEK LOGS
@cli.command()
def week():
    res = requests.get(f"{API_URL}/logs/week")
    logs=res.json()
    display_logs(logs)

if __name__ == "__main__":
    cli()