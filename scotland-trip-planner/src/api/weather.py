#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weather API integration for the Scotland Trip Planner.

This module handles interactions with the Met Office Weather Data API
to retrieve weather forecasts for locations in Scotland.
"""

import requests
from ..config import MET_OFFICE_API_KEY

class WeatherAPI:
    """Class for interacting with the Met Office Weather Data API."""
    
    def __init__(self, api_key=None):
        """Initialize the WeatherAPI with the provided API key."""
        self.api_key = api_key or MET_OFFICE_API_KEY
    
    def get_forecast(self, location_id, resolution="daily"):
        """Get weather forecast for a specific location."""
        # TODO: Implement the API request
        pass
    
    def get_locations(self):
        """Get a list of available locations."""
        # TODO: Implement the API request
        pass