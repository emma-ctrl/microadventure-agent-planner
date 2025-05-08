#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scotland regions data for the Scotland Trip Planner.

This module provides data and functions related to
geographical regions in Scotland.
"""

# Dictionary of Scotland regions with their coordinates (latitude, longitude)
REGIONS = {
    "highlands": {
        "name": "Highlands",
        "center": (57.5, -5.0),
        "description": "The Highlands is a historic region of Scotland.",
    },
    "edinburgh_lothians": {
        "name": "Edinburgh & Lothians",
        "center": (55.95, -3.19),
        "description": "Edinburgh and the Lothians region in Scotland.",
    },
    # Add more regions as needed
}

def get_region(region_id):
    """Get information about a specific region."""
    return REGIONS.get(region_id.lower())

def get_all_regions():
    """Get information about all regions."""
    return REGIONS

def get_nearby_regions(region_id, max_distance=100):
    """Get regions within a certain distance of the specified region."""
    # TODO: Implement distance calculation and filtering
    pass