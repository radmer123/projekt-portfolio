# Dokumentacja interfejsu API Fantasy Football SportsWorldCentral (SWC)
Dziękujemy za korzystanie z interfejsu API SportsWorldCentral. To kompleksowe rozwiązanie dostępu do danych z naszej strony fantasy football, www.sportsworldcentral.com.
## Spis treści
[API publiczne](#api-publiczne)
[Pierwsze kroki](#pierwsze-kroki)
  [Analityka](#analityka)
  [Zawodnik](#zawodnik)
  [Punktacja](#punktacja)
  [Członkostwo](#czlonkostwo)
[Warunki korzystania z usługi](#warunki-korzystania-z-uslugi)
[Przykładowy kod](#przykladowy-kod)
[Zestaw narzędzi programistycznych (SDK)](#zestaw-narzedzi-programistycznych-sdk)

## API publiczne
*Wkrótce dostępne*
Niebawem wdrożymy naszą aplikację. Sprawdź później adres publicznego API.

## Pierwsze kroki
Dziękujemy za korzystanie z API SportsWorldCentral. To Twoje kompleksowe rozwiązanie doostępu do danych z naszej strony internetowej poświęconej rozgrywkom e-sportowym, www.sportsworldcentral.com.

Ponieważ wszystkie dane są publiczne, API SWC nie wymaga żadnego uwierzytelniania. 
Wszystkie poniższe dane są dostępne za pomocą punktów końcowych GET, które zwracają dane w formacie JSON.

### Analityka
Uzyskaj informacje o stanie API oraz liczbie lig, drużyn i zawodników.

### Zawodnik
Możesz pobrać listę wszystkich zawodników NFL lub wyszukać konkretnego zawodnika po jego identyfikatorze (player_id).

### Punktacja
Możesz uzyskać listę wyników zawodników NFL, w tym zdobyte przez nich punkty fantasy według systemu punktacji lig SWC.

### Członkostwo
Uzyskaj informacje o wszystkich ligach fantasy football SWC i drużynach w nich uczestniczących.

## Warunki korzystania
Korzystając z API, zgadzasz się na następujące warunki:
**Limity użytkowania**: Możesz wykonać do 2000 zapytań dziennie. Przekroczenie tego 
                        limitu może skutkować zawieszeniem Twojego klucza API.

**Brak gwarancji**: Nie udzielamy żadnych gwarancji dotyczących działania API.

## Przykładowy kod
Oto przykładowy kod w Pythonie do sprawdzenia stanu API:

```
import httpx
HEALTH_CHECK_ENDPOINT = "/"
    
with httpx.Client(base_url=self.swc_base_url) as client:
    response = client.get(self.HEALTH_CHECK_ENDPOINT)
    print(response.json())
```

## Zestaw narzędzi programistycznych (SDK)
*Wkrótce dostępny*
Sprawdź później, aby uzyskać dostęp do SDK w Pythonie dla naszego API.
