from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Manish Kumar",
    author_email="manish13scme101081@gmail.com",
    packages=find_packages(),
    install_requires=[]
)

"""
🔹 What does this file do (in simple terms)?
👉 It allows your project to be:

installed like a library

reused across environments

deployed on servers (AWS, Docker, CI/CD)

imported cleanly (eg, import medical_chatbot)

Without this file, Python treats your project as just folders, not a package.

-----> One-line summary 
setup.py packages my Medical Chatbot project into an installable Python module, 
enabling clean imports, dependency management, and smooth deployment across environments
like AWS and Docker.

"""