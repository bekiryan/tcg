from setuptools import setup, find_packages

setup(
    name="TCG",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "annotated-types==0.7.0",
        "anyio==4.6.2.post1",
        "certifi==2024.8.30",
        "distro==1.9.0",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.0",
        "idna==3.10",
        "jiter==0.8.0",
        "openai==1.56.1",
        "pydantic==2.10.3",
        "pydantic_core==2.27.1",
        "python-dotenv==1.0.1",
        "sniffio==1.3.1",
        "tqdm==4.67.1",
        "typing_extensions==4.12.2",
    ],
    url="https://github.com/bekiryan/tcg",
)
