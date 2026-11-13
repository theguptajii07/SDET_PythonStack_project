# Playwright Python Test Framework

UI and API test automation for practice applications, built with Python, Playwright and Pytest.

> **Status:** project skeleton. Tests are added one backlog item at a time; see the roadmap below.

## What this tests

- **Web UI:** [SauceDemo](https://www.saucedemo.com), an e-commerce demo app built for automation practice
- **API:** [restful-booker](https://restful-booker.herokuapp.com), a booking API with token authentication and full CRUD

## Tech stack

Python 3.12 · Playwright · Pytest · pytest-playwright

## Prerequisites

- **Python 3.12.** Check with `python --version`. Other 3.x versions may work but aren't tested here.
- **Git.** Check with `git --version`.
- Internet access for the first-time browser download.

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/theguptajii07/SDET_PythonStack_project.git
cd SDET_PythonStack_project
```

**2. Create and activate a virtual environment**

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Your prompt should now start with `(.venv)`.

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Install the Playwright browser**

```bash
playwright install chromium
```

**5. Check that everything is wired up**

```bash
pytest --collect-only
```

At this stage you should see `no tests collected`. That is expected: it means pytest is installed and running correctly, and there are simply no tests yet.

## Project structure

```
.
├── tests/              # Test files
├── .gitignore          # Keeps .venv, caches, reports and secrets out of Git
├── requirements.txt    # Pinned Python dependencies
└── README.md
```

## Troubleshooting

| Problem | Fix |
|---|---|
| PowerShell says running scripts is disabled when activating | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate again |
| `python` is not recognised on Windows | Try `py` instead, or reinstall Python with "Add to PATH" ticked |
| `pytest` or `playwright` is not recognised | The virtual environment isn't active. Repeat step 2 |
| Browser download fails | Check your network or proxy, then rerun `playwright install chromium` |

## Roadmap

- [x] Project skeleton and tooling
- [ ] First Playwright UI test
- [ ] Page Object Model
- [ ] Configuration and environments
- [ ] Data-driven login scenarios
- [ ] End-to-end purchase flow
- [ ] API client for restful-booker
- [ ] API test suite
- [ ] Reporting and failure evidence
- [ ] GitHub Actions pipeline
- [ ] Parallel runs and test markers
- [ ] Containerised test run
- [ ] Architecture notes

## Branching and pull requests

All work happens on `feature/*` branches, merged into `debug` through pull requests. `master` is updated only by release pull requests from `debug`. Both branches are protected against direct pushes.

## Author

theguptajii · [GitHub](https://github.com/theguptajii07)