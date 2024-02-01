import os

def get_windows_username():
    """Retrieves the current Windows username."""

    # Prioritize environment variables for accurate cross-platform compatibility
    username = os.environ.get("USERNAME") or os.environ.get("USER")

    if username:
        return username

    # Fallback to getpass for Windows-specific retrieval if environment variables fail
    import getpass
    username = getpass.getuser()

    return username

# Example usage:
username = get_windows_username()
print("Current Windows username:", username)
