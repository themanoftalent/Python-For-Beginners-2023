
from pkg_resources import get_distribution, DistributionNotFound

from .kml import KML, Document, Folder, Placemark
from .kml import TimeSpan, TimeStamp
from .kml import ExtendedData, Data
from .kml import Schema, SchemaData

from .styles import StyleUrl, Style, StyleMap
from .styles import IconStyle, LineStyle, PolyStyle
from .styles import LabelStyle, BalloonStyle

from .atom import Link, Author, Contributor

try:
    __version__ = get_distribution('fastkml').version
except DistributionNotFound:
    __version__ = 'dev'

__all__ = [
    'KML', 'Document', 'Folder', 'Placemark',
    'TimeSpan', 'TimeStamp',
    'ExtendedData', 'Data',
    'Schema', 'SchemaData',
    'StyleUrl', 'Style', 'StyleMap',
    'IconStyle', 'LineStyle', 'PolyStyle',
    'LabelStyle', 'BalloonStyle',
    'Link', 'Author', 'Contributor',
]
