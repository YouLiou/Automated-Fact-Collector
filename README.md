# 🌍 Automated Fact Collector

This is a digital tool designed to automatically discover, collect, and organize a unique database of interesting facts using Python. This project demonstrates the core principles of automation, data management, and interaction with online APIs.

## Core Functionalities
- **Automation**: Periodically fetches data from an external API without manual intervention.
- **Data Persistence**: Saves collected facts into a local `json` file to maintain a growing knowledge base.
- **Deduplication Logic**: Implements a check to ensure only unique facts are added, preventing duplicates in the database.
- **Structured Data**: Manages information using the JSON format for easy exchange and readability.

## 🛠 Technologies Used
- **Language**: Python 3.14
- **Libraries**: `requests` (API interaction), `json` (data storage), `time` (automation), `os` (file handling)
- **Data Source**: [Useless Facts API](https://uselessfacts.jsph.pl/)

## Project Structure
- `main.py`: The core script containing fetching, saving, and automation logic.
- `fact_archive.json`: The local database storing all unique facts gathered.
- `.gitignore`: Ensures that the virtual environment and temporary files are not tracked.
- `README.md`: Project documentation.

## How to Run
1. Ensure Python 3.14+ is installed on your system.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
