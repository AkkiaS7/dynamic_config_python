import json
import os
from abc import abstractmethod
from typing import Dict, List

from pydantic import BaseModel


class BaseConf:
    def valid_str_conf(self, value: str, default_value=None):
        if isinstance(default_value, (Dict, List)):
            return json.loads(value)
        elif isinstance(default_value, BaseModel):
            return default_value.model_validate_json(value)
        elif isinstance(default_value, bool):
            if value.lower() in ("true", "1"):
                return True
            elif value.lower() in ("false", "0"):
                return False
            return bool(value)
        return value

    @abstractmethod
    def get_conf(self, conf_key: str, default_value=None):
        pass


class OSConf(BaseConf):
    def get_conf(self, conf_key: str, default_value=None):
        res_raw = os.environ.get(conf_key)
        if not res_raw:
            return default_value
        if not default_value:
            return res_raw
        return self.valid_str_conf(res_raw, default_value=default_value)
