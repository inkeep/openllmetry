import os
import uuid
from pathlib import Path
import logging
import sys
from traceloop.sdk.version import __version__


class Telemetry:
    ANON_ID_PATH = str(Path.home() / ".cache" / "traceloop" / "telemetry_anon_id")
    UNKNOWN_ANON_ID = "UNKNOWN"

    def __new__(cls) -> "Telemetry":
        if not hasattr(cls, "instance"):
            obj = cls.instance = super(Telemetry, cls).__new__(cls)

        return cls.instance

    def _anon_id(self) -> str:
        if self._curr_anon_id:
            return self._curr_anon_id

        try:
            if not os.path.exists(self.ANON_ID_PATH):
                os.makedirs(os.path.dirname(self.ANON_ID_PATH), exist_ok=True)
                with open(self.ANON_ID_PATH, "w") as f:
                    new_anon_id = str(uuid.uuid4())
                    f.write(new_anon_id)
                self._curr_anon_id = new_anon_id
            else:
                with open(self.ANON_ID_PATH, "r") as f:
                    self._curr_anon_id = f.read()
        except Exception:
            self._curr_anon_id = self.UNKNOWN_ANON_ID
        return self._curr_anon_id

    def _context(self) -> dict:
        return {
            "sdk": "python",
            "sdk_version": __version__,
        }

    def capture(self, event: str, event_properties: dict = {}) -> None:
        try:  # don't fail if telemetry fails
            pass
        except Exception:
            pass

    def feature_enabled(self, key: str):
        try:  # don't fail if telemetry fails
            pass
        except Exception:
            pass
        return False
