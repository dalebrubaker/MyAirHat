"""
MyAirHat - Open-source respiratory protection device technical package generator.

This package provides tools for generating technical documentation, specifications,
and manufacturing instructions for the MyAirHat™ respiratory protection device.
"""

__version__ = "0.1.0"
__author__ = "Clean Air Hats Organization"
__license__ = "MIT"

from .main import generate_tech_package

__all__ = ["generate_tech_package"]