from setuptools import setup, find_packages

setup(
    name='Nexus Infinity Core',
    version='1.0.0',
    description='A high-tech quantum computing platform',
    long_description='A cutting-edge quantum computing platform for advanced research and development',
    url='https://github.com/KOSASIH/nexus-infinity-core',
    author='KOSASIH',
    author_email='kosasihg88@gmail.com',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'qdk==1.0.0',
        'numpy==1.22.3',
        'pandas==1.3.5',
        'scikit-learn==1.5.0',
        'matplotlib==3.5.1',
        'seaborn==0.11.2',
        'qen-sdk==2.0.0',
        'qen-protocol==1.1.0',
        'qkd-sdk==3.0.0',
        'qkd-protocol==2.0.0',
        'es-sdk==4.0.0',
        'es-protocol==3.0.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='quantum computing qdk qen qkd es',
    project_urls={
        'Bug Reports': 'https://github.com/KOSASIH/nexus-infinity-core/issues',
        'Source': 'https://github.com/KOSASIH/nexus-infinity-core'
    }
)
