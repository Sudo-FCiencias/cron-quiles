"""
Shellaquiles Events - Agregador de feeds ICS públicos de eventos tech en México.
"""

__version__ = "1.0.0"
__author__ = "Shellaquiles Community"

from .ics_aggregator import EventNormalized, ICSAggregator

__all__ = ["ICSAggregator", "EventNormalized"]
