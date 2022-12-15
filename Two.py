import time

def read_file_timed(file):
    start_time = time.time()

    try:
        f = open(file)

    except FileNotFoundError as e:
        print(e)

    else:
        f.read()
        f.close()

    finally:
        time_required = time.time() - start_time
        print(f'Time required for {file} = {time_required}')

video_data = read_file_timed('video.mp4')  #Где надо было брать этот файл?
video_data = read_file_timed('file_not_exist.mp4')