from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent import get_message


EXPECTED = "Hello from Hive!"


def main() -> int:
    actual = get_message()
    score = 1.0 if actual == EXPECTED else 0.0
    print(f"expected={EXPECTED!r}")
    print(f"actual={actual!r}")
    print(f"score={score:.1f}")
    return 0 if score == 1.0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
