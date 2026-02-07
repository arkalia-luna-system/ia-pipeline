"""
Module de démonstration Athalia
"""


def __getattr__(name: str):
    """Import paresseux pour éviter RuntimeWarning avec python -m athalia_core.demo.quickcheck"""
    if name == "quickcheck":
        from .quickcheck import quickcheck

        return quickcheck
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = ["quickcheck"]
