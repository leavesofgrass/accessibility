from distutils.core import setup, Extension
from platform import mac_ver

# Deal with the new location of headers in Mavericks
if mac_ver()[0].startswith('10.9'):
    header_dir = '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/Headers'  # noqa
else:
    header_dir = '/System/Library/Frameworks/ApplicationServices.framework/Frameworks/HIServices.framework/Headers'

setup(
    name = 'accessibility',
    description = 'A Python C Extension that wraps the Accessibility API for Mac OS X.',
    version = '0.2.0',
    author_email = 'atheriel@gmail.com',
    url = 'https://github.com/atheriel/accessibility',
    license = 'ISC',
    platforms = ['MacOS X'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Environment :: MacOS X :: Cocoa',
        'Operating System :: MacOS :: MacOS X',
        'Natural Language :: English',
    ],

    ext_modules = [Extension('accessibility',
        sources = ['accessibility.c'],
        include_dirs = [header_dir],
        # Uncomment the next line to include debug symbols while compiling
        # extra_compile_args = ['-g'],
        extra_link_args = ['-framework', 'ApplicationServices', '-v']
    )],

    install_requires = [
        'docutils>=0.3',
    ]
)