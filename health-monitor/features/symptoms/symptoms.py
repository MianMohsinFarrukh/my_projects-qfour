import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

class SymptomFeature:
    def __init__(self):
        self.symptoms_file = "database/symptoms.txt"

    def symptom_menu(self):
        while True:
            choice = questionary.select(
                "Symptom Menu:",
                choices=[
                    "Add Symptom",
                    "View Symptoms Log",
                    "View Trend Chart",
                    "Back"
                ]
            ).ask()

            if choice == "Add Symptom":
                self.add_symptom()
            elif choice == "View Symptoms Log":
                self.view_symptoms_log()
            elif choice == "View Trend Chart":
                self.view_trend_chart()
            else:
                break

    def add_symptom(self):
        console.print("[bold green]Add New Symptom[/bold green]")
        
        name = questionary.text("Symptom Name:").ask()
        severity = questionary.text("Severity (1-10):").ask()
        description = questionary.text("Description:").ask()
        duration = questionary.text("Duration (in days):").ask()
        started_on = questionary.text("Started On (YYYY-MM-DD):").ask()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.symptoms_file, "a") as f:
            f.write(f"{timestamp},{name},{severity},{description},{duration},{started_on}\n")

        console.print("[bold green]Symptom added successfully![/bold green]")

    def view_symptoms_log(self):
        try:
            with open(self.symptoms_file, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            console.print("[bold red]No symptoms data found.[/bold red]")
            return

        table = Table(title="Symptoms Log")
        table.add_column("Timestamp", style="cyan")
        table.add_column("Symptom", style="magenta")
        table.add_column("Severity", style="magenta")
        table.add_column("Description", style="magenta")
        table.add_column("Duration", style="magenta")
        table.add_column("Started On", style="magenta")

        for line in lines:
            data = line.strip().split(',')
            table.add_row(data[0], data[1], data[2], data[3], data[4], data[5])

        console.print(table)

    def view_trend_chart(self):
        console.print("[bold blue]This feature is under construction.[/bold blue]")
