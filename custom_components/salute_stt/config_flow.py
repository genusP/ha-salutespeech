from typing import TYPE_CHECKING, Any
import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_AUTHENTICATION
from homeassistant.config_entries import ConfigFlowResult
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_AUTHENTICATION): cv.string,
    vol.Optional("cert_path"): cv.string
})

class SaluteConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION="1"

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        if user_input is not None:
            _LOGGER.warn("async_create_entry")
            return self.async_create_entry(
                title="Salute Speech to text", data=user_input
            )

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)
    
    async def async_step_reconfigure(
        self, _: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a reconfiguration flow initialized by the user."""
        entry = self.hass.config_entries.async_get_entry(self.context["entry_id"])

        if TYPE_CHECKING:
            assert entry is not None

        self.entry = entry

        return await self.async_step_reconfigure_confirm()

    async def async_step_reconfigure_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a reconfiguration flow initialized by the user."""
        errors = {}

        if user_input is not None:
            data = {**self.entry.data, **user_input}
            self.hass.config_entries.async_update_entry(self.entry, data=data)
            await self.hass.config_entries.async_reload(self.entry.entry_id)
            return self.async_abort(reason="reconfigure_successful")

        return self.async_show_form(
            step_id="reconfigure_confirm",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )
