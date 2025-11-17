from setuptools import setup, find_packages

setup(
    name='firstdevops-demo',
    version='0.1.0',
    description='A simple Flask app for DevOps demo',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'run-app = main:app.run'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13.3',
)