from questionary import select
from rich.console import Console

console = Console()

from features.vitals.vitals import VitalsFeature
from features.meds.meds import MedicineFeature
from features.symptoms.symptoms import SymptomFeature
from features.ai_assistant.ai_assistant import AIAssistant
from features.export.export import ExportFeature

vitals = VitalsFeature()
meds = MedicineFeature()
symptoms = SymptomFeature()
ai = AIAssistant()
exporter = ExportFeature()

def menu():
    while True:
        choice = select(
            "Select an option:",
            choices=[
                "➕ Add Vitals",
                "📊 View Vitals",
                "💊 Medicines",
                "🩺 Symptoms",
                "🤖 AI Health Assistant",
                "📤 Export Data",
                "❌ Exit"
            ]
        ).ask()

        if choice == "➕ Add Vitals":
            vitals.add_vitals()
        elif choice == "📊 View Vitals":
            vitals.view_vitals()
        elif choice == "💊 Medicines":
            meds.medicine_menu()
        elif choice == "🩺 Symptoms":
            symptoms.symptom_menu()
        elif choice == "🤖 AI Health Assistant":
            ai.daily_health_check()
        elif choice == "📤 Export Data":
            exporter.export_menu()
        else:
            console.print("[red]Goodbye![/red]")
            break

if __name__ == "__main__":
    menu()
