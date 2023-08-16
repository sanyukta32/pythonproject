import pygame
import os


def pause():
    pygame.mixer.music.pause()


def stop():
    pygame.mixer.music.stop()


class MusicPlayer:
    def __init__(self, musicfolder):
        pygame.init()
        pygame.mixer.init()
        self.music_folder = musicfolder
        self.playlist = []
        self.current_song = 0

    def load_playlist(self):
        self.playlist = [song for song in os.listdir(self.music_folder) if song.endswith('.mp3')]

    def play(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            song_path = os.path.join(self.music_folder, self.playlist[self.current_song])
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def next_song(self):
        stop()
        self.current_song = (self.current_song + 1) % len(self.playlist)
        self.play()

    def previous_song(self):
        stop()
        self.current_song = (self.current_song - 1) % len(self.playlist)
        self.play()

    def print_playlist(self):
        for idx, song in enumerate(self.playlist):
            print(f"{idx + 1}. {song}")

    def run(self):
        self.load_playlist()
        self.print_playlist()

        while True:
            print("\nCommands: play, pause, stop, next, prev, exit")
            command = input("Enter a command: ").strip().lower()

            if command == 'play':
                self.play()
            elif command == 'pause':
                pause()
            elif command == 'stop':
                stop()
            elif command == 'next':
                self.next_song()
            elif command == 'prev':
                self.previous_song()
            elif command == 'exit':
                pygame.mixer.music.stop()
                pygame.quit()
                break
            else:
                print("Invalid command. Try again.")


if __name__ == "__main__":
    music_folder = "C:\\Users\\Saura\\PycharmProjects\\pythonProject\\2017"
    player = MusicPlayer(music_folder)
    player.run()
