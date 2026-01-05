import logging
from typing import Any
import voluptuous as vol

from homeassistant.components import tts
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .salute_speech import SaluteSpeechCloud
from .const import CONF_RATE, CONF_VOICE, DEFAULT_LANG, DEFAULT_VOICE, LANGUAGES, MAP_VOICES

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = tts.PLATFORM_SCHEMA.extend({
    # vol.Required(CONF_AUTHENTICATION): cv.string,
    vol.Optional(tts.CONF_LANG, default=DEFAULT_LANG): vol.In(LANGUAGES),
    vol.Optional(CONF_VOICE, default=DEFAULT_VOICE): vol.In(MAP_VOICES['ru-RU'].keys()),
    vol.Optional(CONF_RATE, default='24000'): vol.In(['8000', '24000']),
})


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([SaluteTTS(config_entry)])


class SaluteTTS(tts.TextToSpeechEntity):
    _cloud: SaluteSpeechCloud

    def __init__(self, config_entry: ConfigEntry) -> None:

        self.language: str = "ru"

        self._attr_name = "Salute TTS"
        self._attr_unique_id = f"{config_entry.entry_id[:7]}-ttS"
        self._attr_default_options = {
            CONF_VOICE: DEFAULT_VOICE,
            CONF_RATE: '24000'
        }
        self._cloud = config_entry.runtime_data

    @property
    def default_language(self) -> str:
        return DEFAULT_LANG

    @property
    def supported_languages(self) -> list[str]:
        return LANGUAGES

    @property
    def supported_options(self) -> list[str]:
        return [CONF_VOICE, CONF_RATE]

    @callback
    def async_get_supported_voices(self, language: str) -> list[tts.Voice] | None:
        """Return a list of supported voices for a language."""
        if not (voices := MAP_VOICES.get(language)):
            return None
        return [tts.Voice(voice, name) for voice, name in voices.items()]

    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]):
        _LOGGER.debug('async_get_tts_audio (%s, %s, %s)',
                      message, language, options)
        return await self._cloud.synthesis(message, options.get(CONF_VOICE), options.get(CONF_RATE))
