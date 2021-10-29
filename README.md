# StarTrek-Library-BackEnd
The Library Modules of StarTrek Library. They are **not** executable.

# Language - Sprache
Available in:

[``German``](https://github.com/heschy/StarTrek-Library-BackEnd/tree/German-Deutsch)
[``English``](https://github.com/heschy/StarTrek-Library-BackEnd/tree/main)

## Usage
In order to have an executable application, you have to create a Front-End.
This is the Console-FrontEnd I have used [here](https://github.com/heschy/StarTrek-Library-Console-FrontEnd):

```python
import starfleet;

x = '';

while x != 'cmd(_close_)':
  x = starfleet.library(input('Search for '));
  print('Result:');
  print(x);
```
