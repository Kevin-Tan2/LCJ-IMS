import sys

from PyQt5 import QtWidgets

from masterMaintenance import MasterMaintenance
import pandas as pd


class RWChargeDuration(MasterMaintenance):

    def __init__(self, currentDir=None):

        if currentDir is None:
            currentDir = ""
        else:
            currentDir += "/"

        self.uiFilePath = currentDir + "rwChargeDuration.ui"
        self.csvFilePath = currentDir + "rwChargeDurationList.csv"
        self.columnNames = ['Range of Size', 'Expected Day']

        super().__init__(self.uiFilePath, self.csvFilePath, self.columnNames)

        # sort by Range of Size ascending
        self.df = self.df.sort_values(by='Range of Size')

    def reset_entries(self):
        self.size.clear()
        self.duration.clear()

    def refresh_table(self):
        # sort by Range of Size ascending
        self.df = self.df.sort_values(by='Range of Size')

        super().refresh_table()

    def construct_df(self):
        size = str(self.size.text())
        duration = str(self.duration.text())

        df = pd.DataFrame({'Range of Size': [size], 'Expected Day': [duration]})

        return df

    def add_df(self):
        super().add_df(self.construct_df())

    def save_csv(self):
        super().save_csv(self.csvFilePath)


# to test each module
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = RWChargeDuration()
    widget.show()
    sys.exit(app.exec_())
