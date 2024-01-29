
## Iterators and generators exercise

* Create a generator function that yields the Fibonacci sequence up to a limit that
will be provided as an argument.

* Assume that a function provides to you the contents of a configuration file settings.ini.
In that file, there are different statements for user settings. It is possible to
disable some settings by commenting them by using the hash symbol '#'. Write a generator that returns
only the relevant lines for that file (those that are not commented or empty).
Example file:

```ini
#BEGIN FILE

[Resolution]
Width=1920
Height=1080

[Sound]
Volume=80
Mode=Stereo

#END FILE
```
