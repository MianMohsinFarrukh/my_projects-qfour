import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

class VitalsFeature:
    def __init__(self):
        self.vitals_file = "database/vitals.txt"

    def add_vitals(self):
        console.print("[bold green]Enter Your Vitals[/bold green]")
        
        heart_rate = questionary.text("Heart Rate (bpm):").ask()
        systolic_bp = questionary.text("Systolic BP (mmHg):").ask()
        diastolic_bp = questionary.text("Diastolic BP (mmHg):").ask()
        blood_sugar = questionary.text("Blood Sugar (mg/dL):").ask()
        weight = questionary.text("Weight (kg):").ask()
        temperature = questionary.text("Temperature (°C):").ask()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.vitals_file, "a") as f:
            f.write(f"{timestamp},{heart_rate},{systolic_bp},{diastolic_bp},{blood_sugar},{weight},{temperature}\n")

        console.print("[bold green]Vitals saved successfully![/bold green]")

    def view_vitals(self):
        try:
            with open(self.vitals_file, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            console.print("[bold red]No vitals data found.[/bold red]")
            return

        table = Table(title="Last 7 Days Vitals")
        table.add_column("Timestamp", style="cyan")
        table.add_column("Heart Rate", style="magenta")
        table.add_column("Blood Pressure", style="magenta")
        table.add_column("Blood Sugar", style="magenta")
        table.add_column("Weight", style="magenta")
        table.add_column("Temperature", style="magenta")

        for line in lines[-7:]:
            data = line.strip().split(',')
            table.add_row(data[0], data[1], f"{data[2]}/{data[3]}", data[4], data[5], data[6])

        console.print(table)
