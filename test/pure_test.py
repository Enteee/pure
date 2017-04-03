#!/usr/bin/env python3
# vim: set fenc=utf8 ts=4 sw=4 et :
import unittest
from unittest.mock import MagicMock
from pure import *


class TestPure(unittest.TestCase):

    def test_pure(self):
        fn = MagicMock(
            name = 'fn',
            return_value = True
        )
        fn_wrapped = pure(fn)

        self.assertEqual(fn_wrapped(0), True) 
        self.assertEqual(fn.call_count, 1)

        self.assertEqual(fn_wrapped(0), True) 
        self.assertEqual(fn.call_count, 1)

        self.assertEqual(fn_wrapped(1), True) 
        self.assertEqual(fn.call_count, 2)

    def test_pure_kwargs(self):
        fn = MagicMock(
            name = 'fn',
            return_value = True
        )
        fn_wrapped = pure(fn)

        self.assertEqual(fn_wrapped(test=0), True) 
        self.assertEqual(fn.call_count, 1)

        self.assertEqual(fn_wrapped(test=0), True) 
        self.assertEqual(fn.call_count, 1)

        self.assertEqual(fn_wrapped(test=1), True) 
        self.assertEqual(fn.call_count, 2)

    def test_pure_none_backend(self):
        fn = MagicMock(
            name = 'fn',
            return_value = True
        )
        backend = None
        pure_dec = pure(backend)
        fn_wrapped = pure_dec(fn)

        self.assertEqual(fn_wrapped(0), True) 
        self.assertEqual(fn.call_count, 1)
        self.assertEqual(backend, None)

        self.assertEqual(fn_wrapped(0), True) 
        self.assertEqual(fn.call_count, 2)
        self.assertEqual(backend, None)

        self.assertEqual(fn_wrapped(1), True) 
        self.assertEqual(fn.call_count, 3)
        self.assertEqual(backend, None)

    def test_pure_none_backend_kwargs(self):
        fn = MagicMock(
            name = 'fn',
            return_value = True
        )
        backend = None
        pure_dec = pure(backend)
        fn_wrapped = pure_dec(fn)

        self.assertEqual(fn_wrapped(test=0), True) 
        self.assertEqual(fn.call_count, 1)
        self.assertEqual(backend, None)

        self.assertEqual(fn_wrapped(test=0), True) 
        self.assertEqual(fn.call_count, 2)
        self.assertEqual(backend, None)

        self.assertEqual(fn_wrapped(test=1), True) 
        self.assertEqual(fn.call_count, 3)
        self.assertEqual(backend, None)

    def test_pure_own_backend(self):
        fn = MagicMock(
            name = 'fn',
            return_value = True
        )
        backend = {}
        pure_dec = pure(backend)
        fn_wrapped = pure_dec(fn)

        self.assertEqual(fn_wrapped(0), True) 
        self.assertEqual(fn.call_count, 1)
        self.assertEqual(len(backend), 1)
        self.assertEqual(backend[((0,), frozenset())], True)

        self.assertEqual(fn_wrapped(0), True) 
        self.assertEqual(fn.call_count, 1)
        self.assertEqual(len(backend), 1)
        self.assertEqual(backend[((0,), frozenset())], True)

        self.assertEqual(fn_wrapped(1), True) 
        self.assertEqual(fn.call_count, 2)
        self.assertEqual(len(backend), 2)
        self.assertEqual(backend[((0,), frozenset())], True)
        self.assertEqual(backend[((1,), frozenset())], True)

    def test_pure_own_backend_kwargs(self):
        fn = MagicMock(
            name = 'fn',
            return_value = True
        )
        backend = {}
        pure_dec = pure(backend)
        fn_wrapped = pure_dec(fn)

        self.assertEqual(fn_wrapped(test=0), True) 
        self.assertEqual(fn.call_count, 1)
        self.assertEqual(len(backend), 1)
        self.assertEqual(
            backend[(
                (), 
                frozenset({('test', 0)})
            )
        ], True)

        self.assertEqual(fn_wrapped(test=0), True) 
        self.assertEqual(fn.call_count, 1)
        self.assertEqual(len(backend), 1)
        self.assertEqual(
            backend[(
                (), 
                frozenset({('test', 0)})
            )
        ], True)

        self.assertEqual(fn_wrapped(test=1), True) 
        self.assertEqual(fn.call_count, 2)
        self.assertEqual(len(backend), 2)
        self.assertEqual(
            backend[(
                (), 
                frozenset({('test', 0)})
            )
        ], True)
        self.assertEqual(
            backend[(
                (), 
                frozenset({('test', 0)})
            )
        ], True)

if __name__ == '__main__':
    unittest.main()
