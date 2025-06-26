# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python-based project for the MyAirHat™ fabrication documentation and technical package generation. It contains both a Python package for generating manufacturing documentation and resources for fabricating an innovative respiratory protection device that uses passive molecular diffusion technology.

## Repository Structure

```
MyAirHat/
├── src/myairhat/      # Python package for tech doc generation
├── docs/              # Development documentation and AI discussions
├── photos/            # Product photos and visual guides
├── tech-pkg/          # Generated technical packages for manufacturers
├── LICENSE            # MIT License
├── README.md          # Product overview and project information
├── CLAUDE.md          # This file
├── setup.py           # Python package setup (if created)
└── pyproject.toml     # Python project configuration (if created)
```

## Development Commands

### Setup
```bash
# Create virtual environment (if not automatic)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package in development mode
pip install -e .

# Install development dependencies (once requirements-dev.txt exists)
pip install -r requirements-dev.txt
```

### Running the Code
```bash
# Generate technical package (markdown format)
python -m myairhat.main

# Run as module
python -m myairhat
```

### Future Testing Commands (to be implemented)
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=myairhat

# Type checking
mypy src/myairhat

# Linting
ruff check src/
```

## Key Information

### Product Details
- MyAirHat™ is a physical respiratory protection device, not a software product
- Uses passive molecular diffusion to reduce particle inhalation to 19% (vs 57% for N95 masks)
- Weighs under 5 ounces and made from breathable cotton with clear shield
- Ships in one piece that folds flat into a large shipping envelope
- Currently in prototype stage, not yet government-certified

### Repository Purpose
This repository is intended to document:
- Fabrication and manufacturing processes
- Assembly instructions
- Technical specifications
- Quality control procedures
- Material specifications

## Code Architecture

### Python Package Structure
The `myairhat` package is designed to generate technical documentation for manufacturers:

- `src/myairhat/__init__.py`: Package initialization and exports
- `src/myairhat/main.py`: Main entry point for tech package generation
- Future modules will handle:
  - Bill of materials generation
  - Pattern/template creation (SVG/PNG)
  - Assembly instruction formatting
  - PDF compilation

### Open Source Philosophy
**IMPORTANT**: This is a nonprofit project that ENCOURAGES copying and commercial production:
- All designs are freely available under MIT license
- Manufacturers should feel free to produce and sell MyAirHat™
- Improvements and variations are welcomed
- The goal is maximum public health impact through widespread adoption

## Working with This Repository

### Python Development
- Follow PEP 8 style guidelines
- Add type hints to new functions
- Document all public functions with docstrings
- Keep the package lightweight with minimal dependencies

### Content Organization
- Technical documentation and AI discussions in `docs/`
- Product photos and visual guides in `photos/`
- Generated technical packages in `tech-pkg/`
- Python source code in `src/myairhat/`

### Documentation Standards
- Use clear, technical language appropriate for manufacturers
- Include measurements in both metric and imperial units
- Reference specific materials and suppliers when applicable
- Include version numbers for any technical specifications

### Future Features to Implement
1. Bill of materials generator with cost estimates
2. SVG pattern generator for fabric cutting
3. PDF compilation of complete tech packages
4. Multi-language support for international manufacturers
5. Quality control checklist generator

## Important Notes

- This project combines Python development with physical product documentation
- The product is NOT patent-protected - it's intentionally open for copying
- Encourage manufacturers to produce MyAirHat™ commercially
- More information available at https://www.cleanairhats.org/