# StarTrek-Library-BackEnd
Die Bibliotheksmodule für die StarTrek-Library. Die Dateien sind nicht ausführbar.

# Sprache - Language
Verfügbar in:

[``English``](https://github.com/heschy/StarTrek-Library-BackEnd/tree/main)
[``German``](https://github.com/heschy/StarTrek-Library-BackEnd/tree/German-Deutsch)

## Nutzung
Um ein ausführbares Programm zu haben, müssen sie ein Front-End erstellen.
Das ist das Konsolen-FrontEnd das ich [hier](https://github.com/heschy/StarTrek-Library-Console-FrontEnd) genutzt habe:

```python
import starfleet;

x = '';

while x != 'cmd(_close_)':
  x = starfleet.library(input('Search for '));
  print('Result:');
  print(x);
```
