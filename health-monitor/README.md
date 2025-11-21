PROJECT 01 :

🩺 AI-Powered Personal Health Monitor CLI

A powerful CLI app to track vital tracking, medicine reminders, symptoms analysis, diet suggestions, and AI health insights provide karega — Gemini CLI ki madad se!


Day 1: Setup & Project Base Structure
Step 1 — Install & Learn Gemini CLI
npm install -g @google/gemini-cli
gemini /help
gemini /tools
gemini /memory add “health-monitor rules”

Step 2 — Project Setup
mkdir health-monitor-cli
cd health-monitor-cli

pip install uv
uv init
uv venv
.venv\Scripts\activate

uv add rich questionary

Step 3 — Create Root GEMINI.md

GEMINI.md (root)

# AI-Powered Personal Health Monitor CLI

## Purpose
A CLI-based personal health assistant that:
- Tracks daily health vitals
- Tracks symptoms
- Gives AI-based warnings
- Suggests diet & lifestyle improvements
- Generates health progress reports

## Core Features
- Vital tracking (heart rate, BP, sugar, weight)
- Medicine reminders
- Symptom logging
- AI-based health analysis
- Weekly health report
- Export data (CSV/JSON)
- Streamlit mini dashboard

## Tech Stack
- Python 3.11+
- Gemini CLI (for AI integration)
- Rich (UI)
- Questionary (menus)
- Simple file storage (vitals.txt, symptoms.txt, meds.txt)


Run:

gemini
Prompt: "Read all gemini.md and initialize project structure."
gemini /save setup

Day 2: Vital Tracking System

Create: features/vitals/GEMINI.md

# Vital Tracking Module

## Goal:
User daily vitals track kare:
- Heart rate
- Blood pressure
- Blood sugar
- Weight
- Temperature

## Features:
### Add Vitals:
- Ask each vital
- Validate ranges
- Auto timestamp
- Save in vitals.txt

### View Vitals:
- Last 7 days table
- Color coded (green=normal, yellow=borderline, red=high)

### AI Interpretation:
Gemini ko prompt:
"Analyze today's vitals and give interpretation + warnings."

Output:
- Normal?
- Borderline?
- Action needed?
- Danger alert?

### Trend Analysis:
- Last 7 days averages
- Highest/lowest readings
- Improvement or deterioration


Run:

gemini
Prompt: "Build vitals feature @features/vitals/GEMINI.md"
gemini /save features/vitals

Day 3: Medicine Reminder System

Create: features/meds/GEMINI.md

# Medicine Reminder System

## Features:
### Add Medicine:
- Medicine name
- Dosage
- Frequency (1/day, 2/day)
- Timing
- Start date
- End date

### Today’s Medicines:
- Show all for today with checkboxes

### Mark as Taken:
- Save daily record

### AI Advice:
If medicine missed:
"Give warning + consequences + recovery suggestion."

### Weekly Adherence Report:
- % adherence
- Missed doses
- Improvement tips


Run:

gemini
Prompt: "Add medicine reminder feature. Read @features/meds/GEMINI.md"
gemini /save features/meds

Day 4: Symptom & Health Log

Create: features/symptoms/GEMINI.md

# Symptoms Tracking Module

## Features:
### Add Symptom:
- Symptom name
- Severity 1–10
- Description
- Duration
- Started on
- Save to symptoms.txt

### View Symptoms Log:
- Table
- Trend chart (ASCII bar graph)

### AI Diagnosis Helper:
Prompt:
"Based on symptoms log + vitals, suggest likely issues + urgency level + next steps."


Run:

gemini
Prompt: "Build symptom tracking module @features/symptoms/GEMINI.md"
gemini /save features/symptoms

Day 5: Smart AI Health Assistant

Create: features/ai_assistant/GEMINI.md

# Smart AI Health Assistant

## Features:

### Daily Health Check:
Show:
- Today's vitals status
- Symptoms summary
- Medicines adherence
- AI Health Score

### AI Health Score (0-100):
Factors:
- Vitals stability (30 pts)
- Medicine adherence (30 pts)
- Symptoms severity trend (20 pts)
- Sleep/pain/stress tracking (20 pts)

### Alerts:
- High BP
- High sugar
- Missed medicine
- Persistent symptoms
- Weight gain/loss warning

### Recommendations:
- Diet plan
- Water intake
- Sleep improvement
- Workout suggestion
- Early medical checkup if danger


Run:

gemini
Prompt: "Add AI health assistant features @features/ai_assistant/GEMINI.md"
gemini /save ai/assistant

Day 6: Data Export & Backup

Create: features/export/GEMINI.md

# Data Export & Backup

## Export:
- Export vitals → CSV / JSON
- Export symptoms → CSV / JSON
- Export weekly report → JSON
- Export AI health score

## Backup:
- Auto create backup folder
- Timestamped zip file
- Keep only last 10

## Import:
- Import vitals CSV
- Validate & merge


Run:

gemini
Prompt: "Implement data export features @features/export/GEMINI.md"
gemini /save features/export

Day 7: Streamlit Mini Dashboard
# Web Dashboard (Streamlit)

## Show:
- Health score
- Vitals charts (BP/Sugar trends)
- Symptoms graph
- Medicine adherence %
- Weekly AI summary

## Design:
- Card-based UI
- Green/yellow/red health indicators
- Clean layout

🎉 Final Output

By Day 7 tumhari app:

✔ Full healthcare tracker hogi

✔ Gemini AI-based health assistant hoga

✔ Weekly health report banayegi

✔ Streamlit web dashboard hoga

✔ Export/import/backup system hoga

✔ Portfolio-level healthcare project ban jayega








🩺 AI-Powered Personal Health Monitor CLI — FULL PROJECT SETUP
✅ 1. Complete Folder Structure
health-monitor-cli/
├── GEMINI.md
├── main.py
├── database/
│   ├── vitals.txt
│   ├── symptoms.txt
│   ├── medicines.txt
│   └── backups/
├── features/
│   ├── vitals/
│   │   ├── GEMINI.md
│   │   └── vitals.py
│   ├── meds/
│   │   ├── GEMINI.md
│   │   └── meds.py
│   ├── symptoms/
│   │   ├── GEMINI.md
│   │   └── symptoms.py
│   ├── ai_assistant/
│   │   ├── GEMINI.md
│   │   └── ai_assistant.py
│   └── export/
│       ├── GEMINI.md
│       └── export.py
└── dashboard/
    └── app.py        (Streamlit)

✅ 2. Root Project File — GEMINI.md

⬇️ Ye file Gemini CLI ko project rules & structure sikha deti hai

# AI-Powered Personal Health Monitor CLI

## Objective
Track health vitals, symptoms, medicine reminders and generate AI-based recommendations.

## Modules
- Vitals Tracking
- Symptoms Tracking
- Medicine Reminders
- AI Health Assistant
- Data Export & Backup
- Streamlit Web Dashboard

## Rules
- Use Rich for tables & colors.
- Use Questionary for menus.
- Store data in text files.
- Log all vitals with timestamp.
- Avoid floats for calculations.
- Follow clean OOP modular code.
- Each feature inside /features/<module>.

✅ 3. FULL main.py (Gemini-Ready)
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

✅ 4. Each Feature’s GEMINI.md (Auto Build ke liye Ready)
📌 features/vitals/GEMINI.md
# Vitals Tracking

## Input Fields
- Heart Rate
- Blood Pressure (SYS/DIA)
- Blood Sugar
- Weight
- Temperature
- Auto date/time

## Features
- Add vitals
- View last 7 days
- Trend chart
- AI interpretation

📌 features/meds/GEMINI.md
# Medicines Feature

## Features
- Add medicine
- Today’s medicines
- Mark medicine as taken
- Weekly adherence report
- AI warning for missed doses

📌 features/symptoms/GEMINI.md
# Symptoms Module

## Features
- Add symptom
- Severity (1-10)
- Daily symptoms log
- Trend chart (ASCII)
- AI suggestion based on symptoms + vitals

📌 features/ai_assistant/GEMINI.md
# Smart AI Health Assistant

## Features
- Daily health check
- AI Health Score (0–100)
- Alerts (BP/Sugar high, missed medicine, severe symptoms)
- Health recommendations
- Diet, sleep, hydration suggestions

📌 features/export/GEMINI.md
# Export & Backup System

## Features
- Export vitals CSV/JSON
- Export symptoms CSV/JSON
- Export weekly AI report
- Backup + restore

🟩 5. READY-TO-USE PROMPTS (Gemini CLI)
⭐ Step 1: Project Initialization
gemini
Prompt:
"Read all root GEMINI.md and create project folder structure."

⭐ Step 2: Build Vitals Feature
gemini
Prompt:
"Build vitals feature using @features/vitals/GEMINI.md"

⭐ Step 3: Build Medicine Feature
gemini
Prompt:
"Generate medicine reminder system. Read @features/meds/GEMINI.md"

⭐ Step 4: Build Symptoms Feature
gemini
Prompt:
"Generate symptoms module @features/symptoms/GEMINI.md"

⭐ Step 5: Build AI Assistant
gemini
Prompt:
"Add AI Assistant features. Use @features/ai_assistant/GEMINI.md"

⭐ Step 6: Build Export System
gemini

Prompt:
"Add data export & backup features. Read @features/export/GEMINI.md"

⭐ Step 7: Build Streamlit Dashboard
gemini
Prompt:
"Create streamlit dashboard for vitals, symptoms & health score."