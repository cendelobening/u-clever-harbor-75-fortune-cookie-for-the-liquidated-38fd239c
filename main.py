"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who was just
liquidated, to /output/entry.txt.
"""

import os

LINE = (
    "You will soon meet a tall, dark stranger. "
    "He works in risk management and has already liquidated your portfolio."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
