from setuptools import setup

requirements = ["Django>=3.0.3", "django-extensions>=3.0.9", "pandas>=0.23.4"]

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='jupyterDjangoORM',
  version='0.0.1',
  description='Django Data Navigation With Notebook',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/ThiagueraBarao/jupyterDjangoORM',  
  author='Thiago do Carmo Nunes',
  author_email='thiagocarmonunes@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='django jupyter pandas ORM', 
  packages=['jupyterDjangoORM'],
  install_requires=requirements ,
  zip_safe=False
)