#!/usr/bin/env python2
# -*- coding: utf8 -*-

from __future__ import division, print_function, absolute_import

import io
import os
from StringIO import StringIO

from PIL import Image, ImageEnhance

from walis.config import SOURCE_DIR


def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    assert 0 <= opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


WATERMARK_TMP_DIR = SOURCE_DIR + '/walis/api/handler/cert/watermark/tmp/'


def watermark(image):
    """ watermark image from http.
    """
    # read into PIL
    extension = os.path.splitext(image.filename)[1].lstrip('.')
    return watermark_raw(image.stream.read(), extension)


def watermark_raw(buf, extension):
    """ watermark image from buf bytes.
    """
    if extension.lower() == "jpg":
        extension = "jpeg"

    data_stream = io.BytesIO(buf)
    im = Image.open(data_stream)

    im_wm = watermark_pil(im, opacity=0.5)
    img_io = StringIO()
    im_wm.save(img_io, extension.upper(), quality=70)
    img_io.seek(0)

    return img_io.buf


def watermark_pil(im, mark=None, position='tile', opacity=1):
    """ watermark image from PIL Image obj
    """
    if mark is None:
        mark = Image.open(SOURCE_DIR + '/walis/api/handler/cert/ele_wmark.png')
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark,
                    (int((im.size[0] - w) / 2), int((im.size[1] - h) / 2)))
    else:
        layer.paste(mark, position)
    # composite the watermark with the layer
    return Image.composite(layer, im, layer)