from dataclasses import dataclass
from enum import Enum
from functools import cache
import requests

DOMAIN_NAME = "api.globalping.io"


DEFAULT_BODY = {
    "limit": 1,
    "locations": [],
    "measurement": {
        "query": {"method": "HEAD", "path": "", "protocol": "", "resolver": "74.82.42.42"},
        "type": "http",
        "target": "",
    },
}


class ApiPath(Enum):
    MEASUREMENTS = "/v1/measurements"
    PROBES = "/v1/probes"


class Status(Enum):
    FINISHED = "finished"
    IN_PROGRESS = "in-progress"


@dataclass
class ProbeLocation:
    continent: str
    region: str
    country: str
    city: str
    asn: int
    latitude: float
    longitude: float
    network: str
    state: str = None


@dataclass
class Probe:
    version: str
    ready: bool
    location: ProbeLocation


# Is there a way to not have the `all` variable and have it be the default?
# This dataclasss seems dumb.
@dataclass
class Probes:
    all: list[Probe]

    @cache
    def has_country(self, country: str) -> bool:
        return any(probe.location.country == country for probe in self.all)

    @classmethod
    def generate(cls) -> "Probes":
        probes: list[Probe] = []
        probe_list = requests.get(url=f"https://{DOMAIN_NAME}{ApiPath.PROBES.value}").json()
        for probe in probe_list:
            probes.append(Probe(probe["version"], probe["ready"], ProbeLocation(**probe["location"])))
        return cls(probes)
