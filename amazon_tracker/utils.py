# definition:

# Utility functions in programming are small, reusable pieces of code designed to perform specific, common tasks within a program.
#  They act as helper tools that simplify repetitive or complex operations, such as data manipulation, calculations, string formatting, or input/output handling.
#  These functions are not meant to be standalone but are intended to be used in conjunction with other code to improve overall code organization.

from urllib.parse import urlparse
import re


def is_valid_url(url: str) -> bool:
    try:
        # Parse the URL
        result = urlparse(url)

        # Check if scheme and netloc are present
        if not all([result.scheme, result.netloc]):
            return False

        # Check if scheme is http or https
        if result.scheme not in ["http", "https"]:
            return False

        # Basic regex pattern for domain validation
        domain_pattern = (
            r"^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z]{2,})+$"
        )
        if not re.match(domain_pattern, result.netloc):
            return False

        return True

    except Exception:
        return False