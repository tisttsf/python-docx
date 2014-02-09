# encoding: utf-8

"""
Constants specific the the image sub-package
"""


class JPEG_MARKER_CODE(object):
    """
    JPEG marker codes
    """
    TEM = b'\x01'
    DHT = b'\xC4'
    DAC = b'\xCC'
    JPG = b'\xC8'

    SOF0 = b'\xC0'
    SOF1 = b'\xC1'
    SOF2 = b'\xC2'
    SOF3 = b'\xC3'
    SOF5 = b'\xC5'
    SOF6 = b'\xC6'
    SOF7 = b'\xC7'
    SOF9 = b'\xC9'
    SOFA = b'\xCA'
    SOFB = b'\xCB'
    SOFD = b'\xCD'
    SOFE = b'\xCE'
    SOFF = b'\xCF'

    RST0 = b'\xD0'
    RST1 = b'\xD1'
    RST2 = b'\xD2'
    RST3 = b'\xD3'
    RST4 = b'\xD4'
    RST5 = b'\xD5'
    RST6 = b'\xD6'
    RST7 = b'\xD7'

    SOI = b'\xD8'
    EOI = b'\xD9'
    SOS = b'\xDA'
    DQT = b'\xDB'  # Define Quantization Table(s)
    DNL = b'\xDC'
    DRI = b'\xDD'
    DHP = b'\xDE'
    EXP = b'\xDF'

    APP0 = b'\xE0'
    APP1 = b'\xE1'
    APP2 = b'\xE2'
    APP3 = b'\xE3'
    APP4 = b'\xE4'
    APP5 = b'\xE5'
    APP6 = b'\xE6'
    APP7 = b'\xE7'
    APP8 = b'\xE8'
    APP9 = b'\xE9'
    APPA = b'\xEA'
    APPB = b'\xEB'
    APPC = b'\xEC'
    APPD = b'\xED'
    APPE = b'\xEE'
    APPF = b'\xEF'

    STANDALONE_MARKERS = (
        TEM, SOI, EOI, RST0, RST1, RST2, RST3, RST4, RST5, RST6, RST7
    )

    SOF_MARKER_CODES = (
        SOF0, SOF1, SOF2, SOF3, SOF5, SOF6, SOF7, SOF9, SOFA, SOFB, SOFD,
        SOFE, SOFF
    )

    names = {
        b'\x00': 'UNKNOWN',
        b'\xC0': 'SOF0',
        b'\xC2': 'SOF2',
        b'\xC4': 'DHT',
        b'\xDA': 'SOS',   # start of scan
        b'\xD8': 'SOI',   # start of image
        b'\xD9': 'EOI',   # end of image
        b'\xDB': 'DQT',
        b'\xE0': 'APP0',
        b'\xE1': 'APP1',
        b'\xE2': 'APP2',
        b'\xED': 'APP13',
        b'\xEE': 'APP14',
    }

    @classmethod
    def is_standalone(cls, marker_code):
        return marker_code in cls.STANDALONE_MARKERS


class MIME_TYPE(object):
    """
    Image content types.
    """
    JPEG = 'image/jpeg'
    PNG = 'image/png'


class TAG(object):
    """
    Identifiers for image attribute tags.
    """

    PX_WIDTH = 'px_width'
    PX_HEIGHT = 'px_height'
    HORZ_PX_PER_UNIT = 'horz_px_per_unit'
    VERT_PX_PER_UNIT = 'vert_px_per_unit'
    UNITS_SPECIFIER = 'units_specifier'
