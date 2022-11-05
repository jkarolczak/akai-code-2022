![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)



# Dziel i zwyciężaj (głód)
🦕 paretodactyle

## Opis rozwiązania
### Motywacja

Współczesny świat jest pełen nierówności, które można opisać rozkładem Pareto. 20% ludzi posiada aż 80% majątku. Co za tym idzie, każdego dnia możemy zaobserwować zarówno problem marnowania żywności, jak i głód. Odpowiedzią na te kwestie są jadłodzielnie oraz koncepty food-sharing, jednak nie są one powszechnie znane. Często wiedza o istnieniu np. publicznej lodówki jest znana tylko społeczności osiedla, a osoby potrzebujące nie są świadome ich istnienia.

Nasze rozwiązanie wychodzi z pomocą obu stronom: zarówno tej potrzebującej, jak i dzielącej. Trzy składowe części umożliwiają kompleksową odpowiedź na problem.

### Mapa
Interaktywna mapa zapewnia łatwy dostęp zarówno do lokalnych jadłodzielni, jak również ich zaopatrzenia. Informacja o całkowitym zapełnieniu lodówki w danej jadłodzielni skieruje użytkownika do właściwego punktu oraz uchroni przed przeładowaniem urządzenia. Jednocześnie osoby chcące podzielić się nadmiarową żywnością będą wiedziały do której jadłodzielni się zgłosić.

### Czujnik
Wykorzystanie sensorów umożliwi monitorowanie stanu lodówki oraz przesyłanie danych na serwer w celu ich publikacji. Dodatkowo kontrolują, czy drzwi zostały zamknięte. Gdy drzwi nie zostaną prawidłowo zamknięte, administracja samoobsługowej lodówki zostanie o tym powiadomiona. Dzięki temu opiekun będzie mógł udać się do lodówki, zamknąć ją i zapobiec zepsuciu składowanej żywności. Aby zwrócić uwagę przechodniów, w przypadku pozostawienia otwartych drzwi rozlegnie się syngał dźwiękowy. Warto wspomnieć, że jest to niskokosztowe rozwiązanie, które może zostać wdrożone do istniejących już punktów przy niewielkim nakładzie finansowym. Wystarczy mikrokomputer lub mikrokontroler, kamera oraz czujnik końcowy, a także dostęp do prądu oraz internetu. 

### Detekcja
Dla jadłodzielni z obsługą przygotowany został panel administracyjny, który umożliwia śledzenie stanów magazynów.

Jednak istnieją także jadłodzielnie bezobsługowe, zazwyczaj w formie lodówek. Dzięki uczeniu maszynowemu wykonywana jest detekcja produktów wkładanych do lodówki. Automatycznie kontrolowane jest, czy coś jest wkładane lub wyciągane z lodówki, lecz także kategoria produktu. Pozwala to kontrolować zapełnienie lodówki samoobsługowej bez udziału ludzi. Informacja o zawartości lodówki pomoże potrzebującym i dającym wybrać odpowiedni punkt.

### Konkluzje
Rozkład pareto sugeruje także, że 20% nakładu prac to aż 80% efektu. Przez ostatnie 22 godziny staraliśmy się wykonać choć właśnie te 20%. Zauważyliśmy potrzebę, podzieliliśmy się nia z Wami. Teraz wszystko w naszych rękach. Pamiętajmy o nierównościach za każdym razem, gdy po hackathonie lub zbliżających się świętach zostanie nam dużo jedzenia.


#### Integracja z Too Good To Go
Nasza strona została zintegrowana z API Too Good To Go, dzięki czemu osoby w potrzebie mają szansę kupić produkty w niezwykle okazyjnych cenach oraz ocalić je przed zepsuciem.


## Użytkowanie
Przygotowane rozwiązanie dostępne jest na stronie [http://paretodactyle.pl](http://paratodactyle.pl). Po wejściu ukaże się mapa. Po kliknięciu w pinezkę pojawią się podstawowe informacje o Jadłodzielni. Można z nich przejść do dwóch ekranów. Jeden dedykowany jest użytkownikom i zawiera informacje o zawartości lodówki. Drugi ekran pełni funkcję panelu administracyjnego.

### Demo detekcji jedzenia
https://user-images.githubusercontent.com/82370491/200119839-9db2fa50-1fc1-48dd-9e65-28a5bac98547.MOV
