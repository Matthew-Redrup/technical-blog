# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a technical blog platform that uses nbdev (literate programming with Jupyter notebooks) and FastHTML (Python web framework) to create interactive technical content. The blog focuses on advanced topics in AI, cybersecurity, and software engineering, with the first major topic being Recursive Bayesian Estimators (RBE).

**Key Technologies:**
- **nbdev**: Literate programming - code and documentation in Jupyter notebooks
- **FastHTML**: Modern Python web framework for interactive applications  
- **MonsterUI**: UI component library providing professional styling
- **GitHub Pages**: Automatic documentation hosting from notebooks

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

# Install package in development mode
pip install -e .
```

### FastHTML Development
```bash
# Run the FastHTML web application (from project root)
cd fasthtml_app
python main.py

# Alternative: Run as module (from project root)
python -c "from fasthtml_app.main import app; app.serve()"

# The app will start on FastHTML's default port (usually 5001)
# Check console output for exact URL
```

### Testing and Code Quality
```bash
# Run nbdev tests (includes doctests and notebook tests)
nbdev_test

# Check notebook outputs are clean
nbdev_clean

# Full preparation (export, test, clean) - run before commits
nbdev_prepare
```

## Architecture

### Source Code Structure
- **`nbs/`**: Source notebooks containing both code and documentation
  - `index.ipynb`: Blog homepage (becomes README.md)
  - `00_core.ipynb`, `01_blog_components.ipynb`: Core modules
  - `rbe/`: Recursive Bayesian Estimators series content
  - `future_topics/`: Prepared for additional technical topics
  - `utils/`: Cross-topic utilities
  - Code cells marked with `#| export` are extracted to Python modules

- **`technical_blog/`**: Auto-generated Python package from notebooks
  - **DO NOT edit these files directly** - edit the notebooks instead
  - Auto-updated when running `nbdev_export` or `nbdev_prepare`

- **`fasthtml_app/`**: Interactive web application
  - `main.py`: FastHTML application entry point with MonsterUI theming
  - `components/`: Reusable UI components (rbe/, shared/)
  - `routes/`: URL route handlers (organized by topic)
  - `static/`: CSS, JS, images
  - Uses MonsterUI blue theme for professional appearance

- **`data/`**: Topic-specific datasets and examples
  - `rbe/`: Data for RBE demonstrations and examples

### Development Flow
1. Write content and code in notebooks under `nbs/`
2. Use `#| export` to mark code cells for extraction to Python modules
3. Run `nbdev_export` to generate Python modules in `technical_blog/`
4. Test interactivity in FastHTML app (`python fasthtml_app/main.py`)
5. Use `nbdev_prepare` before committing (exports, tests, cleans notebooks)
6. GitHub Actions automatically builds and deploys documentation

### Key Configuration Files
- **`settings.ini`**: Central configuration for nbdev, dependencies, and project metadata
- **`nbs/_quarto.yml`**: Documentation generation settings  
- **`pyproject.toml`**: Auto-generated from settings.ini
- All package configuration flows through settings.ini

## Content Creation Guidelines

### Blog Posts (Notebooks)
- **Educational Focus**: Explain concepts from fundamentals to advanced applications
- **Interactive Elements**: Use FastHTML components for hands-on exploration
- **Code Quality**: Include type hints, tests, and comprehensive documentation
- **Mathematical Rigor**: Proper derivations with LaTeX rendering
- **Practical Applications**: Real-world examples and performance analysis

### RBE Series Structure
The flagship content covers Recursive Bayesian Estimators:
1. **Fundamentals**: Uncertainty, Bayes' theorem, recursive updating
2. **Applications**: Network anomaly detection, cybersecurity
3. **Advanced Topics**: Multi-model estimation, optimization
4. **Modern Context**: Comparison with deep learning approaches

### FastHTML Components
- Create reusable components in `nbs/01_blog_components.ipynb`
- Export components to `technical_blog.blog_components` module
- Use MonsterUI styling for consistency
- Include interactive demonstrations (particle filters, Bayesian calculators)

## Important Notes

### Development Practices
- **Literate Programming**: Primary development happens in notebooks, not .py files
- **AI-Assisted**: Content created with AI assistance but maintains technical rigor
- **Educational Purpose**: Written to teach the author, shared for community benefit
- **Open Source**: All code available for learning and adaptation
- **Professional Tone**: Approachable but technically accurate

### Technical Standards
- Use FastHTML best practices and modern Python (3.9+)
- Follow nbdev conventions for exports and documentation
- Include comprehensive tests for all algorithms
- Maintain responsive design (mobile-friendly)
- Optimize for both learning and performance

### Workflow Tips
- Always run `nbdev_prepare` before committing
- Test FastHTML app after making component changes
- Use `nbdev_clean` to remove notebook outputs before commits
- Check generated docs at GitHub Pages after pushing

## Dependencies

### Core Requirements (from settings.ini)
- `fastcore pandas numpy scipy matplotlib seaborn plotly ipywidgets python-fasthtml monsterui`

### Development Requirements  
- `jupyter nbdev`

### External Resources
- **Context7 MCP**: Access FastHTML and MonsterUI documentation with "Use Context7"
- **GitHub Repository**: https://github.com/Matthew-Redrup/technical-blog
- **Documentation**: Auto-generated at https://matthew-redrup.github.io/technical-blog/

## Common Tasks

### Adding New Content
1. Create notebook in appropriate `nbs/` subdirectory
2. Add content with `#| export` for reusable code
3. Test in FastHTML app if interactive
4. Run `nbdev_prepare` and commit

### Creating Interactive Components
1. Develop in notebook with FastHTML components
2. Export to `technical_blog` package
3. Import and use in FastHTML app routes
4. Test responsiveness and functionality

### Publishing Updates
1. Commit notebooks with `nbdev_prepare`
2. Push to GitHub (triggers documentation build)
3. Test live site and functionality
4. Share updates and gather feedback
