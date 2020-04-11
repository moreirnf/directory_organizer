import shutil
import time
import os

directory = 'C:/Users/nun0_/Downloads'

actions = [
    (('.png', '.jpg', '.gif'), 'images'),
    (('.mp4', '.mov', '.avi'), 'videos'),
    (('.exe', '.rar', '.zip' , '.msi', '.iso'), 'exe_zip'),
    (('.csv', '.xlsx', 'xls'), 'spreadsheets'),
    (('.json', '.py', '.js', '.sql'), 'scripts_data'),
    (('.wav', '.mp3', '.ogg', '.flac'), 'audio'),
    (('.pdf', '.cbr', '.epub', '.mobi'), 'pdfs+ebooks'),
    (None, 'other')
]


def create_directories(dir):
    for _, dir_name in actions:
        if dir_name not in os.listdir(dir):
            os.mkdir(dir + '/' + dir_name)


def downloads_organizer(dir):
    for file in os.listdir(dir):
        if os.path.isfile(directory + '/' + file):
            src_path = dir + '/' + file
            for extensions, destination in actions:
                if extensions is None or file.endswith(extensions):
                    dest_path = os.path.join(dir, destination, file)
                    shutil.move(src_path, dest_path)
                    break


if __name__ == "__main__":
    try:
        create_directories(directory)
        while True:
            downloads_organizer(directory)
            time.sleep(10)

    except KeyboardInterrupt:
        print('interrupted!')