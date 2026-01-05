"""The Salute STT integration."""

from __future__ import annotations

import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_AUTHENTICATION, Platform
from homeassistant.helpers.typing import ConfigType

from .salute_speech import SaluteSpeechCloud
from .const import CONF_CA_BUNDLE

# type SaluteSpeechConfigEntry = ConfigEntry[]

PLATFORMS = (Platform.STT, Platform.TTS)


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    auth_data = config_entry.data[CONF_AUTHENTICATION]
    cert_path = config_entry.data.get(CONF_CA_BUNDLE)
    speech_api = SaluteSpeechCloud(hass, auth_data, cert_path)
    config_entry.runtime_data = speech_api
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    cloud: SaluteSpeechCloud = config_entry.runtime_data
    if cloud is not None:
        cloud.disconnect()
    return await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
