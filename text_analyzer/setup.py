from setuptools import setup, find_packages

setup(
    name='text_analyzer',            # The name of your package
    version='0.1',                   # The version number
    packages=find_packages(),        # Automatically find and include all packages
    install_requires=[               # Dependencies required by your package
        'spacy',
        'langdetect',
        'os',
        're',
        'fitz',
        'python-docx',
        'collections',
        'langdetect'
        # ... other dependencies ...
    ],
    author='Anatolii Shara',              # Your name
    author_email='anfrankleen23@gmail.com',   # Your email
    description='Text Analyzer Package',  # Short description of your package
    long_description=open('README.md').read(),  # Detailed description from README.md
    url='https://github.com/AnatoliiShara/text_analyzer.git',  # URL to your code repository
    classifiers=[                    # Metadata to classify your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
