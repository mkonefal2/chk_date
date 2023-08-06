import os
import glob
import datetime

path = "/home/valkyrie"
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('**/*.{}'.format(extension), recursive=True)]
result.sort(key=os.path.getmtime, reverse=True)
for file in result:
    file_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    if file_date.date() == datetime.datetime.today().date():
        print(f"{file} - File is up to date", f"- {file_date}")
    else:
        print(f"{file} - file is too old !", f"- {file_date}")
