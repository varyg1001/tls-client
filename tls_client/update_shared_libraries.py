import requests
import platform

shared_library_version = "1.9.1"
github_download_url = "https://github.com//bogdanfinn/tls-client/releases/download/v{}/{}"
github_repo_filenames = [
    # Windows
    f"tls-client-windows-32-{shared_library_version}.dll",
    f"tls-client-windows-64-{shared_library_version}.dll",
    # MacOS
    f"tls-client-darwin-arm64-{shared_library_version}.dylib",
    f"tls-client-darwin-amd64-{shared_library_version}.dylib",
    # Linux
    f"tls-client-linux-alpine-amd64-{shared_library_version}.so",
    f"tls-client-linux-ubuntu-amd64-{shared_library_version}.so",
    f"tls-client-linux-arm64-{shared_library_version}.so"
]
dependency_filenames = [
    # Windows
    "tls-client-32.dll",
    "tls-client-64.dll",
    # MacOS
    "tls-client-arm64.dylib",
    "tls-client-x86.dylib",
    # Linux
    "tls-client-amd64.so",
    "tls-client-x86.so",
    "tls-client-arm64.so"
]

system = platform.system()
if system == "Windows":
    github_repo_filenames = github_repo_filenames[:2]
    dependency_filenames = dependency_filenames[:2]
elif system == "Darwin":
    github_repo_filenames = github_repo_filenames[2:4]
    dependency_filenames = dependency_filenames[2:4]
elif system == "Linux":
    github_repo_filenames = github_repo_filenames[4:]
    dependency_filenames = dependency_filenames[4:]

for github_filename, dependency_filename in zip(github_repo_filenames, dependency_filenames):
    response = requests.get(
        url=github_download_url.format(shared_library_version, github_filename)
    )

    with open(f"dependencies/{dependency_filename}", "wb") as f:
        f.write(response.content)
