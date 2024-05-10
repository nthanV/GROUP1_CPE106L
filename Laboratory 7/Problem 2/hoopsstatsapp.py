from hoopstatsview import HoopStatsView
import pandas as pd

class HoopStatsProcessor:
    def __init__(self, file_path):
     
        self.file_path = file_path
    def load_data(self):
        return pd.read_csv(self.file_path)
    def clean_stats(self, frame):
        unfmtd_clmns = [frame['FG'], frame['3PT'], frame['FT']]
        frame = frame.drop(['FG', '3PT', 'FT'], axis=1)

        for column in unfmtd_clmns:
            column_df = pd.DataFrame(column)
            colname = str(column_df.columns.tolist()[0])  # Get column name
            cleancols = []  # final clean columns
            colnames = [colname + 'M', colname + 'A']

            for entry in column_df.itertuples():
                value = str(tuple(entry)[-1])  # get string entry
                values = value.split('-')  # split with delimiter
                cleancols.append(values)

            cleancols_df = pd.DataFrame(cleancols, columns=colnames)
            index = frame.columns.tolist().index(colname[0:2] + '%')
            frame.insert(index, colnames[0], cleancols_df[colnames[0]])
            frame.insert(index + 1, colnames[1], cleancols_df[colnames[1]])

        return frame

    def run(self):
        frame = self.load_data()
        print("Input:")
        print(frame)
        frame = self.clean_stats(frame)
        print("Cleaned: ")
        print(frame)
        HoopStatsView(frame)

if __name__ == "__main__":
    processor = HoopStatsProcessor("cleanbrogdonstats.csv")
    processor.run()