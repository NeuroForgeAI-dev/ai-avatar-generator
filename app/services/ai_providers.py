"""AI Provider integrations for avatar generation."""
import os
import httpx
from typing import Optional
from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    async def generate_video(self, script: str, **kwargs) -> str:
        pass

    @abstractmethod
    async def synthesize_voice(self, text: str, **kwargs) -> bytes:
        pass


class KlingAIProvider(AIProvider):
    """Kling AI integration for video avatar generation."""

    def __init__(self):
        self.api_key = os.getenv("KLING_API_KEY")
        self.base_url = "https://api.kling.ai/v1"

    async def generate_video(self, script: str, style: str = "business", **kwargs) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/generate",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"script": script, "style": style, "resolution": "1080p"},
                timeout=120,
            )
            response.raise_for_status()
            return response.json()["video_url"]

    async def synthesize_voice(self, text: str, **kwargs) -> bytes:
        raise NotImplementedError("Use ElevenLabsProvider for voice")


class ElevenLabsProvider:
    """ElevenLabs integration for voice synthesis."""

    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.base_url = "https://api.elevenlabs.io/v1"

    async def synthesize(
        self, text: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM",
        language: str = "en", speed: float = 1.0
    ) -> bytes:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/text-to-speech/{voice_id}",
                headers={"xi-api-key": self.api_key},
                json={
                    "text": text,
                    "model_id": "eleven_multilingual_v2",
                    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "speed": speed},
                },
                timeout=60,
            )
            response.raise_for_status()
            return response.content


class HeyGenProvider:
    """HeyGen integration for avatar rendering."""

    def __init__(self):
        self.api_key = os.getenv("HEYGEN_API_KEY")
        self.base_url = "https://api.heygen.com/v2"

    async def create_avatar_video(
        self, audio_url: str, avatar_id: str = "default", background: str = "office"
    ) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/video/generate",
                headers={"X-Api-Key": self.api_key},
                json={"avatar_id": avatar_id, "audio_url": audio_url, "background": background},
                timeout=120,
            )
            response.raise_for_status()
            return response.json()["data"]["video_id"]
