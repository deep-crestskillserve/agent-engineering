#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from stock_picker_mine.crew import StockPickerMine

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the research crew.
    """
    inputs = {
        'sector': 'Technology'
    }

    # Create and run the crew
    result = StockPickerMine().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)


if __name__ == "__main__":
    run()
