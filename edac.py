#!/usr/bin/env python3

import os
import json
import re

DIR = "/sys/devices/system/edac/mc"

DIMM_VARS = [
    "dimm_ce_count",
    "dimm_ue_count",
    "dimm_label",
    "dimm_location",
    "dimm_mem_type",
    "size",
]

MC_VARS = {
    "ce_count",
    "mc_name",
    "size_mb",
    "ue_count",
}


def lst(dir, rgx):
    return [x for x in os.listdir(dir) if re.match(rgx, x)]


def parse(v):
    for t in [int, float]:
        try:
            return t(v)
        except BaseException:
            continue

    return v


def rv(fn):
    with open(fn, "r") as f:
        return parse(f.read().rstrip())


def read_dimm(dir):
    return {x: rv(f"{dir}/{x}") for x in DIMM_VARS}


def read_mc(dir):
    return {x: rv(f"{dir}/{x}") for x in MC_VARS}


r = {}
if os.path.exists(DIR):
    for mc in lst(DIR, r"^mc\d+$"):
        r[mc] = {"dimms": {}, "info": {"mc": mc, **read_mc(f"{DIR}/{mc}")}}
        for dimm in lst(f"{DIR}/{mc}", r"^(dimm|rank)\d+$"):
            r[mc]["dimms"][dimm] = {
                "name": dimm,
                "mc_name": f"{mc}_{dimm}",
                "mc": mc,
                **read_dimm(f"{DIR}/{mc}/{dimm}"),
            }

print(json.dumps(r, indent=2, sort_keys=True))
