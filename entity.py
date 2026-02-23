"""Base entity for the Chandler Systems integration."""

from __future__ import annotations

from homeassistant.components.bluetooth.passive_update_coordinator import (
    PassiveBluetoothCoordinatorEntity,
)
from homeassistant.core import callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo

from .coordinator import ChandlerSystemsCoordinator


class ChandlerSystemsEntity(
    PassiveBluetoothCoordinatorEntity[ChandlerSystemsCoordinator]
):
    """Base entity for Chandler Systems devices."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: ChandlerSystemsCoordinator) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            connections={(dr.CONNECTION_BLUETOOTH, coordinator.address)},
            manufacturer="Chandler Systems",
            name="Chandler Systems Signature",
        )

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()
