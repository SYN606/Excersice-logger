[![Developer](https://img.shields.io/badge/Developer-syn606-ff004c?style=for-the-badge)](https://syn606.pages.dev)
![Maintained](https://img.shields.io/badge/Maintained-Yes-00b300?style=for-the-badge)
![Cross-platform](https://img.shields.io/badge/Cross--platform-Yes-%231e90ff?style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.6%2B-yellow?style=for-the-badge&logo=python)


# Health Management System (Python CLI)

The Health Management System is a command-line application developed in Python for recording, retrieving, and managing user health logs.  
Data is stored in structured JSON files, ensuring easy retrieval, modification, and future extensibility.  
The application uses ANSI escape sequences for colour-coded output, providing clear and user-friendly terminal interactions without external dependencies.

---

## Features
- **Data Entry** – Record a user’s daily meal and exercise information.
- **Data Retrieval** – Display all stored records for a given user in a structured format.
- **Data Deletion** – Permanently remove all stored data for a specific user after confirmation.
- **Colour-Coded Output** – Utilises ANSI escape codes to differentiate prompts, errors, successes, and informational messages.
- **Graceful Exit Handling** – Intercepts `KeyboardInterrupt` (`Ctrl+C`) and `EOFError` (`Ctrl+D`) to terminate cleanly without tracebacks.
- **Modular Architecture** – Core functions are separated into modules to support maintainability and scalability.

---

## Requirements
- **Python**: Version 3.6 or higher
- **Platform**: Compatible with Linux, macOS, and Windows (requires ANSI-compatible terminal on Windows)

---

## Installation
```bash
git clone https://github.com/SYN606/Excersice-logger.git
```

```bash
cd Excersice-logger
```

```bash
python main.py
```
---

## Notes
- Each user’s data is stored as a standalone JSON file inside the data/ directory.

- No external Python packages are required for operation.

- ANSI escape sequences are used for terminal output formatting.

- Ensure your terminal supports ANSI codes (default on Linux/macOS, Windows 10+).
