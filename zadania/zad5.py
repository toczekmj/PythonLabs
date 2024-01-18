class Bug:
    """
    Klasa Bug służy do reprezentowania błędów (bugs) z unikalnym identyfikatorem.
    Zawiera statyczny licznik, który śledzi liczbę stworzonych i aktualnie istniejących obiektów tej klasy.
    """
    counter = 0

    def __init__(self):
        """Inicjalizuje nowy obiekt Bug, zwiększając licznik i przypisując unikalny identyfikator."""
        Bug.counter += 1
        self.id = Bug.counter

    def __del__(self):
        """Usuwa obiekt Bug, zmniejszając licznik i wyświetlając komunikat o usunięciu."""

        Bug.counter -= 1
        print("Koniec, licznik: " + str(Bug.counter) + ", identyifkator: " + str(self.id))

    def __str__(self):
        """Zwraca reprezentację stringową obiektu, pokazującą aktualny licznik i identyfikator."""
        return "Bug: " + str(self.id) + ", counter: " + str(Bug.counter)


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])