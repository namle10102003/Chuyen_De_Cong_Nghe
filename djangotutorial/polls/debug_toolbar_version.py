try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

try:
    v = version('django-debug-toolbar')
    print(f'django-debug-toolbar version: {v}')
except PackageNotFoundError:
    print('django-debug-toolbar is not installed')