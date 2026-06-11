from typing import Iterator, overload


class Playlist:
    def __init__(self, tracks: list[str] | None = None) -> None:
        self._tracks: list[str] = list(tracks) if tracks else []

    def add(self, track: str) -> None:
        self._tracks.append(track)

    def __iter__(self) -> Iterator[str]:
        return iter(self._tracks)

    @overload
    def __getitem__(self, index: int) -> str: ...
    @overload
    def __getitem__(self, index: slice) -> list[str]: ...

    def __getitem__(self, index):
        return self._tracks[index]

    def __len__(self) -> int:
        return len(self._tracks)


def main() -> None:
    playlist = Playlist(["Song A", "Song B", "Song C"])
    playlist.add("Song D")
    print("Итерация:", [track for track in playlist])
    print("По индексу [0]:", playlist[0])
    print("Срез [1:3]:", playlist[1:3])
    print("Длина:", len(playlist))


if __name__ == "__main__":
    main()
