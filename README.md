# Weather MCP Server

A modular FastAPI-based weather server with Docker support.

## Features
- Live weather from OpenWeatherMap
- Dockerized for easy deployment
- Optional cloud deployment (Render, Heroku)

## Getting Started

### Setup

1. Create `.env`:
`OPENWEATHER_API_KEY=your_api_key`
2. Run with Docker:
```
docker build -t weather-mcp .
docker run -d -p 8000:8000–env-file .env weather-mcp
```
3. Access:
`http://localhost:8000/weather?city=Tokyo`

## Deployment

You can deploy this app using Render or Heroku. See instructions in `/docs`.