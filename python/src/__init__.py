
# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences


from pkg_resources import get_distribution, DistributionNotFound
import cv2
import numpy

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __all__ = [cv2, numpy]
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = '1.0'