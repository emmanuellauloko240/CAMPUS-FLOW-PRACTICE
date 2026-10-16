# CAMPUS-FLOW-PRACTICE

# CampusFlow

**A Python-based campus helpdesk and ticket management system.**

CampusFlow is a command-line application designed to help manage campus support requests in one place. It provides a structured way to create tickets, track their status, assign responsibility, and organise support work.

## Problem Statement

Campus support requests can become difficult to track when they are handled informally. Requests may be overlooked, assignments may be unclear, and it can be difficult to understand which issues remain unresolved.

CampusFlow aims to make this process more organised by providing a central system for managing support tickets.

## Features

- **Ticket Management:** Create and manage support tickets.
- **Priority Management:** Organise tickets according to their priority.
- **Ticket Assignment:** Assign tickets to the appropriate person.
- **Status Tracking:** Update ticket statuses as work progresses.
- **Queue Management:** Organise tickets for easier processing.
- **Reports:** Generate summaries of ticket information.
- **JSON Storage:** Store ticket data in JSON files for persistence.
- **Automated Testing:** Use Python's `unittest` framework to verify application behaviour.

## Tech Stack

- **Language:** Python 3
- **Data Storage:** JSON
- **Testing:** `unittest`
- **Version Control:** Git and GitHub

## Getting Started

### Prerequisites

- Python 3 installed on your computer.
- Git installed on your computer.

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate into the project directory:

   ```bash
   cd campusflow-next
   ```

3. Run the application:

   ```bash
   python3 main.py
   ```

Follow the prompts displayed in the terminal to interact with the application.

## Running Tests

Run the test suite from the project root:

```bash
python3 -m unittest discover -v
```

This runs the tests discovered by Python's `unittest` framework. Review the output to identify any failing tests.

## Project Structure

```text
campusflow-next/
├── main.py              # Application entry point
├── ticket.py            # Ticket-related logic
├── workflow.py          # Ticket workflow operations
├── storage.py           # Data persistence
├── report.py            # Reporting functionality
├── tickets.json         # Stored ticket data
├── test_ticket.py       # Ticket tests
├── test_workflow.py     # Workflow tests
├── ai-learning-log.md   # AI learning documentation
├── baseline-check.md    # Baseline testing notes
└── docs/                # Project documentation
```

*The structure above reflects the main files in the project; update it if your repository changes.*

## What I Learned

Working on CampusFlow provides practical experience with:

- Designing reusable Python functions.
- Working with dictionaries and lists.
- Validating input and handling errors.
- Separating application logic into modules.
- Reading and writing JSON files.
- Writing unit tests and investigating bugs.
- Using Git and GitHub to manage project changes.

## Future Improvements

Potential improvements include:

- Adding more comprehensive validation and edge-case tests.
- Improving error handling during file loading and saving.
- Adding a web-based interface.
- Introducing user authentication and role-based permissions.
- Expanding reports with more detailed ticket statistics.

## Project Status

CampusFlow is a learning project under development. Features and implementation details may evolve as the application improves.

## Author

Developed as a practical project to strengthen Python programming and software engineering skills.
