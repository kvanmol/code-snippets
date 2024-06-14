import pandas as pd
from typing import Dict, Any

class Pipeline:
    def __init__(self, extract, transform, load):
        """
        Initialize the pipeline with extract, transform, and load stages.

        :param extract: Extract function.
        :param transform: Transform function.
        :param load: Load function.
        """
        self.extract = extract
        self.transform = transform
        self.load = load

    def run(self, sources: Dict[str, Any], destinations: Dict[str, Any]) -> None:
        """
        Execute the pipeline.

        :param sources: Dictionary containing information about data sources.
        :param destinations: Dictionary containing information about data destinations.
        """
        data = self.extract(sources)
        data = self.transform(data)
        self.load(data, destinations)