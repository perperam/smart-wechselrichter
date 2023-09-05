import csv
import time
from datetime import datetime
from pathlib import Path

import inverters
from inverters import Test


class DataRecorder:
    def __init__(self, inverter: inverters.Inverter, interval=10, path='./'):
        self.inverter = inverter
        self.interval = interval
        self.path = path

        self._init_paths()
        self._run()

    def _init_paths(self) -> None:
        """
        Initialize the paths where the collected data from the inverters is saved.
        Later there should be a logic if two prevent collision if two inverters have the same name
        :return:
        """
        path_data_dir = Path(self.path) / 'data'

        if not path_data_dir.exists():
            path_data_dir.mkdir(parents=True)

        self.path_csv = path_data_dir / f'{self.inverter.name.lower()}.csv'

    def _run(self) -> None:
        # Open the CSV file in append mode with newline='' to avoid extra line breaks
        with open(self.path_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            print('checking file headers')

            # Write header if the file is empty
            if file.tell() == 0:
                print('no header found in file, catch first data')
                while True:
                    data = self.inverter.get_data()
                    if data != None:
                        csv_columns = ['time'] + list(data.keys())
                        print(f'new header: {csv_columns}')
                        writer.writerow(csv_columns)
                        break

        print('file headers found, started recording')
        while True:
            # Get the current time
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Get data from the get_data() function
            data = self.inverter.get_data()

            # Create a tuple with current time and data
            row = (current_time,) + tuple(data.values())

            with open(self.path_csv, mode='a', newline='') as file:
                writer = csv.writer(file)

                # Write the tuple to the CSV file
                writer.writerow(row)

                # Flush the file to make sure the data is written immediately
                file.flush()

            time.sleep(self.interval)
