from setuptools import setup, find_packages
# partie configuration
setup(
    name="emailer",
    version="0.1",
    author="Nicaisse Bryan et Jean Ritchy-Bastien",
    author_email="bryannicaisse2001@gmail.com",
    description="Un module Python pour envoyer des emails facilement",
    long_description=open(
        "README.md"
    ).read(),  # Description détaillée depuis le fichier README
    long_description_content_type="text/markdown",
    url="https://github.com/Nicaisse/emailer_py.git",
    packages=find_packages(),  # Recherche automatique des packages à inclure
    install_requires=[
        "smtplib",
        "email",
    ],
)
