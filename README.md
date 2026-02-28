# 🎭 AI Avatar Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-0.104+-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/React-18+-61DAFB?logo=react" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

> Generate realistic AI digital avatars with custom voice for business marketing, presentations, and social media.

## 🚀 Features

- **Text-to-Avatar**: Upload a script, get a talking avatar video
- **Voice Synthesis**: Custom voice via ElevenLabs API
- **Multiple Styles**: Business, Casual, Creative avatar presets
- **Batch Processing**: Generate multiple avatars in parallel
- **REST API**: Full FastAPI backend with OpenAPI docs
- **React Dashboard**: Modern UI for managing avatar generation

## 📦 Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3.10+, FastAPI, Celery |
| Frontend | React 18, TypeScript, Tailwind |
| AI/ML | Kling AI, HeyGen, ElevenLabs |
| Database | PostgreSQL, Redis |
| Deploy | Docker, docker-compose |

## 🏗️ Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  React UI   │────▶│  FastAPI      │────▶│  Celery      │
│  Dashboard  │     │  REST API    │     │  Workers     │
└─────────────┘     └──────────────┘     └─────────────┘
                           │                     │
                    ┌──────┴──────┐        ┌─────┴─────┐
                    │  PostgreSQL │        │  AI APIs   │
                    │  + Redis    │        │  Kling/HG  │
                    └─────────────┘        └───────────┘
```

## ⚡ Quick Start

```bash
# Clone
git clone https://github.com/NeuroForgeAI-dev/ai-avatar-generator.git
cd ai-avatar-generator

# Setup environment
cp .env.example .env
# Edit .env with your API keys

# Run with Docker
docker-compose up -d

# Or run locally
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/avatars/generate` | Create new avatar |
| GET | `/api/v1/avatars` | List all avatars |
| GET | `/api/v1/avatars/{id}` | Get avatar details |
| GET | `/api/v1/avatars/{id}/status` | Check generation status |
| DELETE | `/api/v1/avatars/{id}` | Delete avatar |

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

Built with ❤️ by [NeuroForge AI](https://github.com/NeuroForgeAI-dev)
