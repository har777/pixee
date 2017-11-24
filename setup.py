from distutils.core import setup

setup(
    name='pixee',
    version='0.2',
    py_modules=['pixee'],
    author='Harikrishnan Shaji',
    author_email='hihari777@gmail.com',
    url='https://github.com/har777/pixee',
    description='View images and gifs in iTerm2',
    download_url='https://github.com/har777/pixee/archive/0.2.tar.gz',
    entry_points='''
        [console_scripts]
        pixee=pixee:display
    ''',
    install_requires=[
        'requests',
    ],
)
