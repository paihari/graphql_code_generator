from setuptools import setup, find_packages

setup(
    name='graphql_code_generator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'graphene',
        'graphql',
    ],
    entry_points={
        'console_scripts': [
            'generate_code=graphql_code_generator.generate_code:main'
        ]
    }
)
