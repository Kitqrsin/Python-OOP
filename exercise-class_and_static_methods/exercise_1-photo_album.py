class PhotoAlbum:
    COUNT_OF_PHOTOS = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list = [[] for el in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count//4)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < PhotoAlbum.COUNT_OF_PHOTOS:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page+1} slot {self.photos[page].index(label)+1}"

        return "No more free slots"

    def display(self):
        result = '-----------'
        for row in range(len(self.photos)):
            photos_on_a_row = ["[]" for el in range(len(self.photos[row]))]

            result += f'\n{" ".join(photos_on_a_row)}\n'
            result += '-----------'
        return result


album = PhotoAlbum.from_photos_count(0)
print(album.photos)
print(album.add_photo("lol"))