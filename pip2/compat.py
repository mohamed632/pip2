"""Stuff that differs in different Python versions."""

# Try importing the non-stdlib version of the library (distutils2) first to
# allow newer versions to override older functionality in the standard library.
try:
    import distutils2 as packaging
    import distutils2.database
    import distutils2.install
    import distutils2.pypi
except ImportError:
    # Initially planned for the Python 3.3 standard library, but yanked out
    # because it wasn't ready. This is left here in case it goes back in for
    # Python 3.4.
    #import packaging
    #import packaging.database
    #import packaging.install
    #import packaging.pypi
    raise

# Try importing the non-stdlib version of mock first to allow newer versions to
# override older functionality in the standard library.
try:
    import mock
except ImportError:
    try:
        # Available in the standard library in Python 3.3+
        import unittest.mock as mock
    except ImportError:
        # Mock isn't needed for normal functionality, so don't worry if it
        # can't be imported here; the tests will complain if they need it
        pass
