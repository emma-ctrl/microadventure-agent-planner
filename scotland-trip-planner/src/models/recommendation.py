#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recommendation data structures for the Scotland Trip Planner.

This module defines classes for representing trip recommendations
that combine location, weather, and route information.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional
from .location import Location
from .weather import WeatherForecast
from .route import Route

@dataclass
class Recommendation:
    """Class for representing a trip recommendation."""
    
    location: Location
    weather: WeatherForecast
    routes: List[Route] = field(default_factory=list)
    score: float = 0.0
    date: datetime = field(default_factory=datetime.now)
    additional_info: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        """Return a string representation of the recommendation."""
        return f"Recommendation: {self.location.name} (Score: {self.score:.1f})"

@dataclass
class RecommendationSet:
    """Class for representing a set of trip recommendations."""
    
    recommendations: List[Recommendation] = field(default_factory=list)
    creation_date: datetime = field(default_factory=datetime.now)
    user_preferences: Dict[str, Any] = field(default_factory=dict)
    
    def add_recommendation(self, recommendation: Recommendation) -> None:
        """Add a recommendation to the set."""
        self.recommendations.append(recommendation)