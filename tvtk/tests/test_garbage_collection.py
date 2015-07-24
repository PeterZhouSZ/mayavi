""" Tests for the garbage collection of objects in tvtk package.
"""
# Authors: Deepak Surti, Ioannis Tziakos
# Copyright (c) 2015, Enthought, Inc.
# License: BSD Style.

import unittest
from traits.etsconfig.api import ETSConfig

from tvtk.pyface.scene import Scene
from tvtk.pyface.scene_model import SceneModel
from tvtk.tests.common import TestGarbageCollection

class TestTVTKGarbageCollection(TestGarbageCollection):
    """ See: tvtk.tests.common.TestGarbageCollection
    """
    
    @unittest.skipIf(
        ETSConfig.toolkit=='wx', 'Test segfaults using WX (issue #216)')
    def test_scene(self):
        """ Tests if Scene can be garbage collected."""
        def obj_fn():
            return Scene()

        def close_fn(o):
            o.closed = True

        self.check_object_garbage_collected(obj_fn, close_fn)
    
    def test_scene_model(self):
        """ Tests if SceneModel can be garbage collected."""
        def create_fn():
            return SceneModel()

        def close_fn(obj):
            obj.closed = True

        self.check_object_garbage_collected(create_fn, close_fn)
