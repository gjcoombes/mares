#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: models.py
Created on Wed Dec 18 11:47:55 2013
@author: gcoombes
Description:
Models for the runsets app.
A combination
"""
### Imports
from __future__ import print_function

import redis

### Logging ###
import logging
logging.basicConfig(level=logging.DEBUG)
debug, info, error = logging.debug, logging.info, logging.error

### Constants
REDIS_HOST = "tornado"
REDIS_PORT = 6379
REDIS_DB = 1
### Classes

def redis_connection(r_conn=None, host=None, port=None, db=None):
    """Return a new redis connection if required"""
    if r_conn is None:
        _host = host or REDIS_HOST
        _port = port or REDIS_PORT
        _db   = db   or REDIS_DB
        r = redis.StrictRedis(host=_host, port=_port, db=_db)
    else:
        r = r_conn
    return r

class RunSet(object):
    """
    Represents one redis set
    e.g. j0282:wahanda:running
    """

    def __init__(self, group, machine, phase, r_conn=None):
        self._group = group
        self._machine = machine
        self._phase = phase
        self._conn = r_conn or redis_connection()

    def __eq__(self, other):
        """Equal if same key and underlying redis instance"""
        return all([
                self.group == other.group,
                self.machine == other.machine,
                self.phase == other.phase,
            ])

    def __repr__(self):
        """ e.g. RunSet("test", "wahanda", "running") """
        return 'RunSet("{o.group}", "{o.machine}", "{o.phase}")'.format(o=self)

    def __str__(self):
        return ":".join([self.group, self.machine, self.phase])

    def __unicode__(self):
        return u":".join([self._group, self._machine, self._phase])


    @property
    def key(self):
        return str(self)

    @property
    def group(self):
        return self._group

    @property
    def machine(self):
        return self._machine

    @property
    def phase(self):
        return self._phase

    @property
    def conn(self):
        return self._conn

    @property
    def members(self):
        return self.conn.smembers(self.key)

    def is_member(self, stem):
        return self.conn.sismember(self.key, stem)

    def add(self, stem):
        self.conn.sadd(self.key, stem)

    def delete(self, stem):
        self.conn.delete(self.key, stem)




### Functions

### Tests
def xtest_suite():
    test_runset_key()
    test_runset_group()
    test_runset_setter()
    test_runset_members()
    test_runset_is_member()
    test_runset_add_member()
    test_runset_delete()
    test_runset_repr()
    test_runset_roundtrip()
    test_runset_equals_true()

def test_runset_key():
    r = RunSet("trial", "wahanda", "running")
    assert r.key == "trial:wahanda:running"

def test_runset_group():
    r = RunSet("trial", "wahanda", "running")
    assert r.group == "trial"

def test_runset_setter():
    r = RunSet("trial", "wahanda", "running")
    try:
        r.group = "asa"
    except AttributeError:
        pass

def test_runset_members():
    r = RunSet("j0282", "wahanda", "running")
    map(print, r.members)

def test_runset_is_member():
    r = RunSet("j0282", "wahanda", "running")
    assert not r.is_member("monkeys")

def test_runset_add_member():
     r = RunSet("test", "wahanda", "running")
     r.add("monkeys")
     assert r.is_member("monkeys")

def test_runset_delete():
     r = RunSet("test", "wahanda", "running")
     r.add("monkeys")
     assert r.is_member("monkeys")
     r.delete("monkeys")
     assert not r.is_member("monkeys")

def test_runset_repr():
    r = RunSet("test", "wahanda", "running")
    expected = 'RunSet("test", "wahanda", "running")'
    assert repr(r) == expected

def test_runset_roundtrip():
    r = RunSet("test", "wahanda", "running")
    new_r = eval(repr(r))
    assert isinstance(new_r, RunSet)

def test_runset_equals_true():
    r1 = RunSet("test", "wahanda", "running")
    r2 = RunSet("test", "wahanda", "running")
    assert r1 == r2

if __name__ == "__main__":
    # test_suite()

















    print("Done __main__")
