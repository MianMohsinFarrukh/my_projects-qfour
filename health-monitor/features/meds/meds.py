import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

class MedicineFeature:
    def __init__(self):
        self.medicines_file = "database/medicines.txt"

    def medicine_menu(self):
        while True:
            choice = questionary.select(
                "Medicine Menu:",
                choices=[
                    "Add Medicine",
                    "View Today's Medicines",
                    "Mark as Taken",
                    "View Adherence Report",
                    "Back"
                ]
            ).ask()

            if choice == "Add Medicine":
                self.add_medicine()
            elif choice == "View Today's Medicines":
                self.view_today_medicines()
            elif choice == "Mark as Taken":
                self.mark_as_taken()
            elif choice == "View Adherence Report":
                self.view_adherence_report()
            else:
                break

    def add_medicine(self):
        console.print("[bold green]Add New Medicine[/bold green]")
        
        name = questionary.text("Medicine Name:").ask()
        dosage = questionary.text("Dosage:").ask()
        frequency = questionary.text("Frequency (e.g., 1/day, 2/day):").ask()
        timing = questionary.text("Timing (e.g., after breakfast):").ask()
        start_date = questionary.text("Start Date (YYYY-MM-DD):").ask()
        end_date = questionary.text("End Date (YYYY-MM-DD):").ask()

        with open(self.medicines_file, "a") as f:
            f.write(f"{name},{dosage},{frequency},{timing},{start_date},{end_date}\n")

        console.print("[bold green]Medicine added successfully![/bold green]")

    def view_today_medicines(self):
        console.print("[bold blue]This feature is under construction.[/bold blue]")

    def mark_as_taken(self):
        console.print("[bold blue]This feature is under construction.[/bold blue]")

    def view_adherence_report(self):
        console.print("[bold blue]This feature is under construction.[/bold blue]")
