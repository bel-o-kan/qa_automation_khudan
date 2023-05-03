from abc import ABC , abstractmethod


class Artwork(ABC) :
    def __init__(self , artist , title , year) :
        self._artist = artist
        self._title = title
        self._year = year

    @abstractmethod
    def display(self) :
        pass

    @property
    def artist(self) :
        return self._artist

    @artist.setter
    def artist(self , new_artist) :
        self._artist = new_artist

    @property
    def title(self) :
        return self._title

    @title.setter
    def title(self , new_title) :
        self._title = new_title

    @property
    def year(self) :
        return self._year

    @year.setter
    def year(self , new_year) :
        self._year = new_year


class Painting(Artwork) :
    def __init__(self , artist , title , year , canvas_type) :
        super().__init__(artist , title , year)
        self._canvas_type = canvas_type

    def display(self) :
        print(
            f"This is a painting called '{self._title}', created by {self._artist} in {self._year} on {self._canvas_type} canvas.")


class Sculpture(Artwork) :
    def __init__(self , artist , title , year , material) :
        super().__init__(artist , title , year)
        self._material = material

    def display(self) :
        print(
            f"This is a sculpture called '{self._title}', created by {self._artist} in {self._year} from {self._material}.")


class Photograph(Artwork) :
    def __init__(self , artist , title , year , subject) :
        super().__init__(artist , title , year)
        self._subject = subject

    def display(self) :
        print(
            f"This is a photograph called '{self._title}', created by {self._artist} in {self._year} of {self._subject}.")


# Create instances of each class
mona_lisa = Painting("Leonardo da Vinci" , "Mona Lisa" , 1503 , "poplar")
david = Sculpture("Michelangelo" , "David" , 1504 , "marble")
moonrise = Photograph("Ansel Adams" , "Moonrise, Hernandez" , 1941 , "a small town in New Mexico")

# Call display method for each instance
mona_lisa.display()
david.display()
moonrise.display()

# Update some properties
mona_lisa.title = "La Gioconda"
david.year = 1501

# Display updated properties
print(mona_lisa.title)
print(david.year)
