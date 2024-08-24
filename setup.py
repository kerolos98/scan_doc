from setuptools import setup, find_packages


setup(
    name='scan_doc',
    version='0.1',
    packages=find_packages(),
    install_requires=['matplotlib','numpy','opencv-python','scipy'],  # Use the list of dependencies from requirements.txt
    include_package_data=True,
    description='A brief description of my package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='kerolos emad',
    author_email='kemad57@gmail.com',
)
