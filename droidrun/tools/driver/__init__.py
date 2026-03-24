"""Device driver abstractions for DroidRun."""

from importlib import import_module

from droidrun.tools.driver.android import AndroidDriver
from droidrun.tools.driver.base import DeviceDisconnectedError, DeviceDriver
from droidrun.tools.driver.ios import IOSDriver
from droidrun.tools.driver.recording import RecordingDriver
from droidrun.tools.driver.stealth import StealthDriver

__all__ = [
    "DeviceDisconnectedError",
    "DeviceDriver",
    "AndroidDriver",
    "CloudDriver",
    "IOSDriver",
    "RecordingDriver",
    "StealthDriver",
]


def __getattr__(name: str):
    if name == "CloudDriver":
        try:
            return import_module("droidrun.tools.driver.cloud").CloudDriver
        except ImportError as exc:
            raise ImportError(
                "CloudDriver requires the optional cloud dependencies. "
                "Install droidrun[cloud] to enable MobileRun support."
            ) from exc
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
