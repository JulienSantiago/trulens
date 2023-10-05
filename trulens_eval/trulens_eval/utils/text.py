"""
Utilities for user-facing text generation.
"""

import logging
import sys

logger = logging.getLogger(__name__)


if hasattr(sys.stdout, "reconfigure"):
    # Some stdout can't handle the below emojis (like terminal). This will skip over the emoji printing
    sys.stdout.reconfigure(errors="replace")


UNICODE_STOP = "🛑"
UNICODE_CHECK = "✅"
UNICODE_YIELD = "⚡"
UNICODE_HOURGLASS = "⏳"
UNICODE_CLOCK = "⏰"
UNICODE_SQUID = "🦑"
UNICODE_LOCK = "🔒"
