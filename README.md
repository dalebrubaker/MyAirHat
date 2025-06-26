# MyAirHat™ Fabrication Project

## Overview

This repository contains resources and information for the fabrication of MyAirHat™, an innovative respiratory protection device that provides superior particle filtration compared to traditional N95 masks while maintaining comfort and visibility.

**This is an open-source project by Clean Air Hats, a nonprofit organization. We encourage manufacturers worldwide to copy, improve, and produce MyAirHat™ freely to save lives and protect public health.**

## About MyAirHat™

MyAirHat™ is a lightweight, reusable respiratory protection device that creates a "separated air environment" around the wearer's face. Unlike traditional masks that rely on a tight facial seal, MyAirHat uses passive molecular diffusion technology to reduce particle inhalation to just 19% (compared to 57% with N95 masks).

## Key Features

- **Superior Protection**: Reduces particle inhalation more effectively than N95 masks
- **Integrated Face Shield**: Protects eyes from airborne particles
- **Enhanced Communication**: Clear shield allows lip-reading and facial expression visibility
- **Lightweight Design**: Weighs under 5 ounces
- **Comfortable Materials**: Made from soft, breathable cotton fabric
- **Reusable & Sustainable**: Can be washed and dried for repeated use
- **No Facial Seal Required**: Gentle breathing environment without pressure buildup

## Technical Specifications

- **Construction**: Breathable cotton fabric with clear shield window
- **Assembly**: Ships in one piece that folds flat into a large shipping envelope
- **Weight**: Under 5 ounces
- **Use Environment**: Designed for indoor/moderate temperature use
- **Maintenance**: Can be dried overnight to deactivate viruses

## Fabrication Details

This project focuses on the manufacturing and assembly processes for MyAirHat™ components:

- Fabric cutting and sewing patterns
- Shield attachment methods
- Quality control procedures
- Assembly instructions

## Design Innovation

MyAirHat™ employs passive molecular diffusion technology to create a protective air environment without requiring a tight facial seal. This innovative approach allows for:

- Natural breathing without pressure buildup
- Brief eating/drinking without full removal
- Adjustable shield fit for different face shapes

## Project Status

MyAirHat™ is currently in prototype stage. While not yet government-certified, independent laboratory testing demonstrates significant protection advantages over traditional mask designs.

## Open Source Philosophy

As a nonprofit organization, Clean Air Hats believes in maximizing public health impact through open collaboration. We explicitly:

- **Encourage copying**: Please take our designs and improve them
- **Support commercial production**: Manufacturers can freely produce and sell MyAirHat™
- **Welcome improvements**: Share your enhancements to help save more lives
- **Provide full documentation**: Technical packages, patterns, and specifications are freely available

Our goal is widespread adoption to protect as many people as possible from airborne particles.

## Technical Documentation

This repository includes a Python package (`myairhat`) for generating technical documentation packages for manufacturers. These packages will include:

- Complete bill of materials with specifications
- Cutting patterns and templates (SVG/PNG formats)
- Step-by-step assembly instructions
- Quality control checklists
- Supplier recommendations
- Manufacturing best practices

### Getting Started

```bash
# Clone the repository
git clone https://github.com/dalebrubaker/MyAirHat.git
cd MyAirHat

# Create virtual environment (if not automatic)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package (once setup.py is configured)
pip install -e .

# Generate technical package
python -m myairhat.main
```

## Repository Structure

```
MyAirHat/
├── src/myairhat/      # Python package for tech doc generation
├── docs/              # Development documentation and AI discussions
├── photos/            # Product photos and visual guides
├── tech-pkg/          # Generated technical packages for manufacturers
├── LICENSE            # MIT License
└── README.md          # This file
```

## Contributing

We welcome contributions! Whether you're a manufacturer with production insights, a designer with improvements, or a developer enhancing the documentation tools, your input helps save lives.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. This means you can freely use, modify, and distribute this work, even commercially.

## More Information

For additional details about MyAirHat™, visit [www.cleanairhats.org](https://www.cleanairhats.org/)
