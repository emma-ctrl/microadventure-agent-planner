#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiking route data structures for the Scotland Trip Planner.

This module defines classes for representing hiking routes
and related information.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from .location import Coordinates

@dataclass
class RoutePoint:
    """Class for representing a point on a hiking route."""
    
    coordinates: Coordinates
    elevation: float  # in meters
    distance: float  # distance from start in kilometers

@dataclass
class Route:
    """Class for representing a hiking route."""
    
    name: str
    region: str
    start_point: Coordinates
    end_point: Coordinates
    length: float  # in kilometers
    ascent: float  # in meters
    difficulty: str  # e.g., "Easy", "Moderate", "Hard"
    estimated_time: float  # in hours
    route_url: str
    description: Optional[str] = None
    points: List[RoutePoint] = field(default_factory=list)
    features: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        """Return a string representation of the route."""
        return f"{self.name} ({self.length}km, {self.difficulty})"