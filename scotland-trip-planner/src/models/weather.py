#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weather data structures for the Scotland Trip Planner.

This module defines classes for representing weather forecasts
and conditions for locations in Scotland.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional

@dataclass
class WeatherCondition:
    """Class for representing a specific weather condition."""
    
    temperature: float  # in Celsius
    precipitation_probability: float  # 0-100%
    wind_speed: float  # in km/h
    wind_direction: str  # e.g., "N", "SW"
    humidity: float  # 0-100%
    visibility: str  # e.g., "VG" (very good), "PO" (poor)
    weather_type: str  # e.g., "Sunny", "Cloudy", "Rain"

@dataclass
class WeatherForecast:
    """Class for representing a weather forecast for a location."""
    
    location_name: str
    location_id: str
    forecast_date: datetime
    conditions: Dict[datetime, WeatherCondition] = field(default_factory=dict)
    
    def add_condition(self, time: datetime, condition: WeatherCondition) -> None:
        """Add a weather condition for a specific time."""
        self.conditions[time] = condition
    
    def get_condition(self, time: datetime) -> Optional[WeatherCondition]:
        """Get the weather condition for a specific time."""
        return self.conditions.get(time)