import asyncio

from viam.module.module import Module

try:
    from models.discovery import PrinterDiscovery  # noqa: F401
    from models.printer import Printer  # noqa: F401
except ModuleNotFoundError:
    from .models.discovery import PrinterDiscovery  # noqa: F401
    from .models.printer import Printer  # noqa: F401


if __name__ == "__main__":
    asyncio.run(Module.run_from_registry())
