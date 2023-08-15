#!/usr/bin/env python3

def _get_code_from_file(fname):
    # Check for a compiled file first
    with open(fname, "rb") as f:
        code = read_code(f)
    if code is None:
        # That didn't work, so try it as normal source code
        with open(fname, "rU") as f:
            code = compile(f.read(), fname, 'exec')
            assert 1 == 2, "custom error message: 1 is not equal to 2"