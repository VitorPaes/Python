#PT.1

# Load numpy as np and pandas as pd
import numpy as np
import pandas as pd

# Create class: DataShell
class DataShell:
    def __init__(self, inputFile):
        self.file = inputFile

# Instantiate DataShell as my_data_shell
my_data_shell = DataShell(us_life_expectancy)

# Print my_data_shell
print(my_data_shell)

#PT.2

# Load numpy as np and pandas as pd
import numpy as np
import pandas as pd

# Create class: DataShell
class DataShell:
    def __init__(self, inputFile):
        self.file = inputFile

# Create class CsvDataShell, which inherits from DataShell
class CsvDataShell(DataShell):
    # Initialization method with arguments self, inputFile
    def __init__(self, inputFile):
        # Instance variable data
        self.data = pd.read_csv(inputFile)

# Instantiate CsvDataShell as us_data_shell, passing us_life_expectancy as argument
us_data_shell = CsvDataShell(us_life_expectancy)
