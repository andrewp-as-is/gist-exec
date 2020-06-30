import setuptools

setuptools.setup(
    name='gist-exec',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/gist-exec']
)
