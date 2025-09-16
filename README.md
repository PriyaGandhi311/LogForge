# 🧠 LogForge

**LogForge** is a Python-powered system inspection and logging pipeline designed for Linux environments. It collects detailed system metrics—CPU, memory, disk, and network—and stores them in a SQLite database using a custom logging handler. A Streamlit dashboard provides a clean, interactive interface to visualize logs in real time.

---

## 🐧 Built for Linux, Powered by Python

This project is optimized for Linux-based systems and leverages Python’s `psutil`, `logging`, and `sqlite3` modules to extract and persist system-level insights. Whether you're monitoring a dev server, inspecting a container, or building reproducible workflows, LogForge gives you structured visibility into your machine.

---

## 🚀 Features

- 🧩 Modular Python scripts for system inspection
- 🗃️ SQLite-backed logging with timestamped entries
- 📊 Streamlit dashboard for log visualization
- 🐚 Bash script for one-command execution (`run_all.sh`)
- 🔒 Designed for reproducibility and CLI integration

---

## 📦 Requirements

- Python 3.8+
- Linux (tested on Ubuntu, Debian, and Arch)
- `psutil`, `streamlit`, `tabulate`

Install dependencies:
pip install -r requirements.txt

---

## Dashboard preview
<img src="log_sql_pipeline/dashboard_preview.png" alt="LogForge Dashboard Preview" width="600" height="500"/>

## 🔍 What Makes LogForge Unique
- Linux-first design: Tailored for terminal workflows, cron jobs, and containerized environments.
- Python-powered modularity: Built with clean, extensible scripts using psutil, logging, and sqlite3.
- Structured logging: Stores logs in a SQLite database for easy querying, analysis, and archiving.

Whether you're inspecting a dev server, monitoring a container, or building reproducible workflows, LogForge turns system noise into structured insight.

## 📜 License
This project is licensed under the **MIT License**.