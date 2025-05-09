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
docker run -p 8000:8000 weather-mcp-server
```
3. Access:
`http://localhost:8000/weather?city=Tokyo`

## How to Get an OPENWEATHER_API_KEY

To use this project, you need an API key from OpenWeather. Follow these steps to obtain one:

1. Go to the [OpenWeather website](https://openweathermap.org/).
2. Sign up for a free account or log in if you already have one.
3. Navigate to the "API Keys" section in your account dashboard.
4. Generate a new API key or use an existing one.
5. Copy the API key and add it to the `.env` file in the project root as follows:

```
OPENWEATHER_API_KEY=your_api_key_here
```

## Deployment

You can deploy this app using Render or Heroku. See instructions in `/docs`.