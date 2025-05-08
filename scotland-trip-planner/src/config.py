#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration management for the Scotland Trip Planner.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
MET_OFFICE_API_KEY = os.getenv("MET_OFFICE_API_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Configuration
DEFAULT_REGION = os.getenv("DEFAULT_REGION", "highlands")
MAX_DRIVING_DISTANCE = int(os.getenv("MAX_DRIVING_DISTANCE", "200"))  # in kilometers