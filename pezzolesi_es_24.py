class Film:
    def __init__(self, titolo, regista, anno, genere, rating):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere
        self.rating = rating

    def __str__(self):
        return f"{self.titolo} ({self.anno}) di {self.regista} - {self.genere} - Rating: {self.rating}"

    def get_rating(self):
        return self.rating


class FilmLibrary:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def search_by_title(self, title):
        return [film for film in self.films if title.lower() in film.titolo.lower()]

    def search_by_director(self, director):
        return [film for film in self.films if director.lower() in film.regista.lower()]

    def display_all_films(self):
        for film in self.films:
            print(film)

    def average_rating(self):
        if not self.films:
            return 0
        total_rating = sum(film.get_rating() for film in self.films)
        return total_rating / len(self.films)


def main():
    library = FilmLibrary()

    while True:
        print("\nFilm Library Menu:")
        print("1. Add Film")
        print("2. Search by Title")
        print("3. Search by Director")
        print("4. Display All Films")
        print("5. Average Rating")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            titolo = input("Enter film title: ")
            regista = input("Enter director: ")
            anno = input("Enter release year: ")
            genere = input("Enter genre: ")
            rating = float(input("Enter rating: "))
            film = Film(titolo, regista, anno, genere, rating)
            library.add_film(film)
            print("Film added successfully.")

        elif choice == '2':
            title = input("Enter title to search: ")
            results = library.search_by_title(title)
            if results:
                print("Search Results:")
                for film in results:
                    print(film)
            else:
                print("No films found.")

        elif choice == '3':
            director = input("Enter director to search: ")
            results = library.search_by_director(director)
            if results:
                print("Search Results:")
                for film in results:
                    print(film)
            else:
                print("No films found.")

        elif choice == '4':
            print("All Films:")
            library.display_all_films()

        elif choice == '5':
            avg_rating = library.average_rating()
            print(f"Average Rating: {avg_rating:.2f}")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
