"""
Droidrun - A framework for controlling Android devices through LLM agents.
"""

import logging
from importlib import import_module
from importlib.metadata import version

__version__ = version("droidrun")

# Attach a default CLILogHandler so that every consumer (CLI, TUI, SDK,
# tools-only) gets visible output without explicit setup.  CLI and TUI
# replace this with their own handler via ``configure_logging()``.
from droidrun.log_handlers import CLILogHandler

_logger = logging.getLogger("droidrun")
_logger.addHandler(CLILogHandler())
_logger.setLevel(logging.INFO)
_logger.propagate = False

# Make main components available at package level
__all__ = [
    # Agent
    "DroidAgent",
    "load_llm",
    "ResultEvent",
    # Tools / Drivers
    "DeviceDriver",
    "AndroidDriver",
    "RecordingDriver",
    # Macro
    "MacroPlayer",
    "replay_macro_file",
    "replay_macro_folder",
    # Configuration
    "DroidrunConfig",
    "AgentConfig",
    "FastAgentConfig",
    "ManagerConfig",
    "ExecutorConfig",
    "ScripterConfig",
    "AppCardConfig",
    "DeviceConfig",
    "LoggingConfig",
    "TracingConfig",
    "TelemetryConfig",
    "ToolsConfig",
    "CredentialsConfig",
    "SafeExecutionConfig",
    "LLMProfile",
]


_LAZY_EXPORTS = {
    "ResultEvent": ("droidrun.agent", "ResultEvent"),
    "DroidAgent": ("droidrun.agent.droid", "DroidAgent"),
    "load_llm": ("droidrun.agent.utils.llm_picker", "load_llm"),
    "DeviceDriver": ("droidrun.tools", "DeviceDriver"),
    "AndroidDriver": ("droidrun.tools", "AndroidDriver"),
    "RecordingDriver": ("droidrun.tools", "RecordingDriver"),
    "MacroPlayer": ("droidrun.macro", "MacroPlayer"),
    "replay_macro_file": ("droidrun.macro", "replay_macro_file"),
    "replay_macro_folder": ("droidrun.macro", "replay_macro_folder"),
    "DroidrunConfig": ("droidrun.config_manager", "DroidrunConfig"),
    "AgentConfig": ("droidrun.config_manager", "AgentConfig"),
    "FastAgentConfig": ("droidrun.config_manager", "FastAgentConfig"),
    "ManagerConfig": ("droidrun.config_manager", "ManagerConfig"),
    "ExecutorConfig": ("droidrun.config_manager", "ExecutorConfig"),
    "ScripterConfig": ("droidrun.config_manager", "ScripterConfig"),
    "AppCardConfig": ("droidrun.config_manager", "AppCardConfig"),
    "DeviceConfig": ("droidrun.config_manager", "DeviceConfig"),
    "LoggingConfig": ("droidrun.config_manager", "LoggingConfig"),
    "TracingConfig": ("droidrun.config_manager", "TracingConfig"),
    "TelemetryConfig": ("droidrun.config_manager", "TelemetryConfig"),
    "ToolsConfig": ("droidrun.config_manager", "ToolsConfig"),
    "CredentialsConfig": ("droidrun.config_manager", "CredentialsConfig"),
    "SafeExecutionConfig": ("droidrun.config_manager", "SafeExecutionConfig"),
    "LLMProfile": ("droidrun.config_manager", "LLMProfile"),
}


def __getattr__(name: str):
    if name in _LAZY_EXPORTS:
        module_name, attr_name = _LAZY_EXPORTS[name]
        value = getattr(import_module(module_name), attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(list(globals().keys()) + __all__)
