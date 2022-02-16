import ffmpeg
import os


def video_to_gif_converter(file, fps, resolution):
    # Открываем файл для преобразования
    stream = ffmpeg.input("Videos/" + file)
    # Вытаскиваем разрешение из файла
    probe = ffmpeg.probe("Videos/" + file)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    # Модифицируем разрешение в соответствии с запросом пользователя
    width = int(video_stream['width']) * resolution
    height = int(video_stream['height']) * resolution
    # Выставляем количество кадров в секунду и разрешение гифки
    stream = ffmpeg.filter(stream, "fps", fps=fps)
    stream = ffmpeg.filter(stream, 'scale', width=width, height=height)
    # Ставим папку Gifs и файл .gif с тем же именем, как точку выхода
    gif_file = "Gifs/" + file.split('.')[0] + ".gif"
    stream = ffmpeg.output(stream, gif_file)
    ffmpeg.run(stream)


def main():
    fps = input("Введите, сколько кадров в секунду вы хотите в гифке: ")
    resolution = float(input("Введите, сколько процентов от изначального будет разрешение гифки: "))
    resolution *= 0.01
    # Проходимся по каждому файлу в папке "видео", передавая его в метод
    for file in os.listdir("Videos"):
        video_to_gif_converter(str(file), fps, resolution)


if __name__ == "__main__":
    main()
