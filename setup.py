from setuptools import setup, find_packages
 
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
  packages=find_packages(),
  install_requires=['pandas','json','django','django-extensions'] 
)