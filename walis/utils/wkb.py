# coding=utf8

from __future__ import absolute_import, division, print_function

import binascii
import io
import itertools
import json
import struct

from geoalchemy2 import (
    Geometry,
    Geography,
    WKBElement,
)

SRID = 4326

LITTLE_ENDIAN = 1
BIG_ENDIAN = 0

WKB_POINT = 1
WKB_LINE_STRING = 2
WKB_POLYGON = 3


def geojson_to_wkbelement(geojson):
    return WKBElement(WKBWriter(geojson).hex_wkb, srid=SRID)


class BinCoder(object):
    def __init__(self, order_byte):
        if isinstance(order_byte, bytes):
            self.order = struct.unpack(">B", order_byte)
        else:
            self.order = order_byte
        self.order_marker = '>' if self.order == BIG_ENDIAN else '<'

    def encode(self, fmt, *values):
        return struct.pack("{}{}".format(self.order_marker, fmt), *values)

    def decode(self, fmt, *values):
        return struct.unpack("{}{}".format(self.order_marker, fmt), *values)[0]


class WKBReader(object):
    """
    convert hex wkb to geojson
    """
    def __init__(self, h):
        self.reader = io.BytesIO(binascii.unhexlify(h))
        self.coder = BinCoder(self.reader.read(1))
        self.order = self.coder.order

        _type = self.coder.decode('i', self.reader.read(4))
        self.geometry_type = _type & 0xff
        self.dim = 3 if ((_type & 0x80000000) != 0) else 2

        self.SRID = -1
        if (_type & 0x20000000) != 0:
            self.SRID = self.coder.decode('i', self.reader.read(4))

        geometry_map = {
            WKB_POINT: self._read_point,
            WKB_LINE_STRING: self._read_line_string,
            WKB_POLYGON: self._read_polygon,
        }

        self.coordinates = geometry_map[self.geometry_type]()

    @property
    def geojson(self):
        if self.geometry_type == WKB_POINT:
            return {"type": "Point", "coordinates": self.coordinates}
        elif self.geometry_type == WKB_LINE_STRING:
            return {"type": "LineString", "coordinates": self.coordinates}
        elif self.geometry_type == WKB_POLYGON:
            return {"type": "Polygon", "coordinates": self.coordinates}

    def _read_coordinate(self):
        return tuple(self.coder.decode('d', self.reader.read(8))
                     for i in range(self.dim))

    def _read_point(self):
        return self._read_coordinate()

    def _read_line_string(self):
        size = self.coder.decode('i', self.reader.read(4))
        return tuple(self._read_coordinate() for i in range(size))

    def _read_polygon(self):
        rings = self.coder.decode('i', self.reader.read(4))
        return tuple(self._read_line_string() for i in range(rings))


class WKBWriter(object):
    """
    convert geojson to wkb
    """
    def __init__(self, geojson, byte_order=LITTLE_ENDIAN):
        self.coder = BinCoder(byte_order)

        self.buf = [self.coder.encode('B', byte_order)]

        geojson = json.loads(geojson)
        self.coordinates = geojson["coordinates"]
        if geojson["type"] == "Point":
            self._type = WKB_POINT
            self.dim = len(self.coordinates)
            self._write_point()
        elif geojson["type"] == "Polygon":
            self._type = WKB_POLYGON
            self.dim = len(self.coordinates[0][0])
            self._write_polygon()

    @property
    def wkb(self):
        return b''.join(self.buf)

    @property
    def hex_wkb(self):
        return ''.join(['\\x', binascii.hexlify(self.wkb).decode("utf-8")])

    def _write_type(self):
        if self.dim == 3:
            self._type |= 0x80000000
        self.buf.append(self.coder.encode('i', self._type))

    def _write_coordinate_sequence(self, seq, write_size):
        if write_size:
            self.buf.append(self.coder.encode('i', len(seq)))

        for coord in itertools.chain(*seq):
            self.buf.append(self.coder.encode('d', coord))

    def _write_point(self):
        self._write_type()
        seq = [self.coordinates]
        self._write_coordinate_sequence(seq, False)

    def _write_polygon(self):
        self._write_type()
        self.buf.append(self.coder.encode('i', len(self.coordinates)))
        for ring in self.coordinates:
            self._write_coordinate_sequence(ring, True)
