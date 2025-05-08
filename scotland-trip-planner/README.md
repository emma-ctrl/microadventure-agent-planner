# Scotland Trip Planner

A Python application to help users find ideal locations for weekend trips in Scotland based on weather, driving distances, and hiking routes.

## Features

- Weather forecast integration using Met Office Weather Data API
- Driving distance and route planning with Google Maps API
- Hiking route information scraped from Walk Highlands
- Recommendation engine that combines all data sources
- (Optional) Web interface for easy interaction

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your API keys
6. Run the application: `python src/main.py`

## Project Structure

- `src/`: Source code
  - `api/`: External API integrations
  - `data/`: Web scraping and data processing
  - `models/`: Data structures
  - `engine/`: Recommendation system
  - `utils/`: Helper functions
- `tests/`: Unit tests
- `web/`: Web interface (optional)

## Dependencies

See `requirements.txt` for a full list of dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.