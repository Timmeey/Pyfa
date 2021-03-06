"""
Since fighter abilities do not have any sort of item entity in the EVE database, we must derive the abilities from the
effects, and thus this effect file contains some custom information useful only to fighters.
"""
from eos.types import State

# User-friendly name for the ability
displayName = "Warp Disruption"

prefix = "fighterAbilityWarpDisruption"

type = "active", "projected"

def handler(fit, src, context):
    if "projected" not in context: return
    fit.ship.increaseItemAttr("warpScrambleStatus", src.getModifiedItemAttr("{}PointStrength".format(prefix)))