#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Location and coordinate data structures for the Scotland Trip Planner.

This module defines classes for representing geographical locations
and coordinates in Scotland.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional, Tuple

@dataclass
class Coordinates:
    """Class for representing geographical coordinates."""
    
    latitude: float
    longitude: float
    
    def __str__(self):
        """Return a string representation of the coordinates."""
        return f"{self.latitude:.6f}, {self.longitude:.6f}"

@dataclass
class Location:
    """Class for representing a geographical location in Scotland."""
    
    name: str
    coordinates: Coordinates
    region: str
    description: Optional[str] = None
    amenities: Dict[str, Any] = field(default_factory=dict)
    driving_distances: Dict[str, float] = field(default_factory=dict)
    
    def __str__(self):
        """Return a string representation of the location."""
        return f"{self.name} ({self.coordinates})"