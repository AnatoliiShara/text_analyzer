from setuptools import setup, find_packages

setup(
    name='text_analyzer',            # The name of your package
    version='0.1',                   # The version number
    packages=find_packages(),        # Automatically find and include all packages
    install_requires=[               # Dependencies required by your package
        'spacy',
        'langdetect',
        # ... other dependencies ...
    ],
    author='Your Name',              # Your name
    author_email='your@email.com',   # Your email
    description='Text Analyzer Package',  # Short description of your package
    long_description=open('README.md').read(),  # Detailed description from README.md
    url='https://github.com/yourusername/text_analyzer',  # URL to your code repository
    classifiers=[                    # Metadata to classify your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
