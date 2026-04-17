# Agent Instructions for ekstedts-katalogen

## ⚙️ Operational Gotchas
- **Core Tool Dependency:** The project heavily relies on the external command-line tool `docling` for data ingestion.
- **Execution:** Data processing is performed by executing `docling <pdf_path>` via `ingest.py`. Execution ofall python scrips is done using `uv`
- **Prerequisite:** Ensure `docling` is installed and available in the system's PATH before running ingestion scripts.

## 📁 Structure & Entry Points
- **Main Entry:** `main.py` serves as a simple application entry point.
- **Ingestion Logic:** The primary data processing logic is contained in `ingest.py`, which handles PDF processing using `docling`.
