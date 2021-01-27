#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the {{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_')}} module.
"""
import pytest

import {{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_')}}


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_{{ cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_')}}(an_object):
    assert an_object == {}
