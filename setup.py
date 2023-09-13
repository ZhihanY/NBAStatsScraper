from setuptools import setup, find_packages

setup(
    name='NBAStatsScraper',
    version='0.2',
    author='Zhihan Yang',
    description= "A Python Client for scraping stats from multiple NBA websites",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'numpy==1.22.1',
        'pandas==1.4.0',
        'requests==2.27.1',
        'unidecode==1.2.0',
        'gspread==5.11.1',
        'gspread-dataframe==3.3.1'
        ]
)