# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a technical blog platform that uses nbdev (literate programming with Jupyter notebooks) and FastHTML (Python web framework) to create interactive technical content. The blog focuses on advanced topics in AI, cybersecurity, and software engineering.

## Development Commands

### nbdev Workflow
```bash
# Export notebooks to Python modules
nbdev_export

# Prepare for git commit (export, test, clean notebooks)
nbdev_prepare

# Build documentation
nbdev_docs

# Run tests
nbdev_test

# Clean notebooks (remove outputs)
nbdev_clean
```

### FastHTML Development
```bash
# Run the FastHTML web application
python -m fasthtml_app.main

# The app will start on http://localhost:5001
```

### Testing and Linting
```bash
# Run pytest
pytest

# Format code with black
black technical_blog/
black fasthtml_app/
```

## Architecture

### Source Code Structure
- **`nbs/`**: Source notebooks containing both code and documentation
  - Notebooks with numbered prefixes (00_, 01_) are core modules
  - Code cells marked with `#| export` are extracted to Python modules
  - Series content goes in subdirectories (e.g., `nbs/rbe/`)

- **`technical_blog/`**: Auto-generated Python package from notebooks
  - DO NOT edit these files directly - edit the notebooks instead

- **`fasthtml_app/`**: Web application for serving interactive content
  - `main.py`: FastHTML application entry point
  - `components/`: Reusable UI components
  - `routes/`: URL route handlers
  - Uses MonsterUI theme (blue variant)

### Development Flow
1. Write content and code in notebooks under `nbs/`
2. Use `#| export` to mark code cells for extraction
3. Run `nbdev_export` to generate Python modules
4. Test interactivity in FastHTML app
5. Use `nbdev_prepare` before committing

### Key Configuration
- **`settings.ini`**: Central configuration for nbdev, dependencies, and project metadata
- **`_quarto.yml`**: Documentation generation settings
- All package configuration flows through settings.ini

## Important Notes
- This is a literate programming project - primary development happens in notebooks
- The FastHTML app provides interactive demonstrations alongside the notebook content
- When adding new features, create notebooks first, then export to Python modules
- The project uses AI assistance for content creation but maintains rigorous technical standards
- Use the fastai coding style

## Context7 Access
- Access documentation for FastHtml and MonsterUI through the Context7 MCP with the command "Use Context7"

## Repository Information
- GitHub repo is https://github.com/Matthew-Redrup/technical-blog