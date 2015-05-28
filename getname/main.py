#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    main.py
    ~~~~~~~~

    some help functions.

    :copyright: (c) 2015 by lord63.
    :license: MIT, see LICENSE for more details.
"""

from __future__ import absolute_import, unicode_literals

import random
import json
from os import path
from itertools import chain


_ROOT = path.abspath(path.dirname(__file__))


class UniqueRandomArray(object):
    """Get consecutively unique elements from an array."""
    def __init__(self, sequence):
        self.previous = None
        self.sequence = sequence

    def rand(self):
        item = random.choice(self.sequence)
        if item == self.previous:
            item = self.rand()
        self.previous = item
        return item


def load_names(the_type):
    """Load names from the json file."""
    json_file = path.join('data', the_type + '_names.json')
    with open(path.join(_ROOT, json_file)) as f:
        names = json.load(f)
    return names


def generate_random_name(the_type, gender=None, showall=False):
    """Generate a name or print them all according to the type."""
    names = load_names(the_type)
    if the_type == 'dog':
        if showall:
            if gender in ['female', 'male']:
                return '\n'.join(names[gender])
            else:
                return '\n'.join(chain(*names.values()))
        else:
            if gender:
                random_name = UniqueRandomArray(names[gender]).rand()
                return random_name
            else:
                all_names = list(chain(*names.values()))
                random_name = UniqueRandomArray(all_names).rand()
                return random_name
    elif the_type in ['cat', 'superhero', 'supervillain']:
        if gender:
            return "{0} has no gender at all.".format(the_type)
        else:
            if showall:
                return '\n'.join(names)
            else:
                random_name = UniqueRandomArray(names).rand()
                return random_name
    else:
        return ("I don't know about {0}, "
                "try cat/dog/hero/villain.".format(the_type))
