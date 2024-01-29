
## Object orientation exercise

* Write a `Track` class, representing an audio track on some sound medium. Give
  the class two attributes, one describing the track, and another specifying the
  length of the track (in minutes).

* Make sure the class has an `__init__` method, and that instances of it can be
  created, and have the right values.

* Write a `CD_ROM` class, representing a 74 minute writable compact disc with
  tracks on it. Wait with the attributes for a while, but give it an empty
  `__init__` method for now. Make sure the class can be instantiated.

* Now implement the following three methods (and add member-variables as needed):
    * `add_track` (which adds a track to the CD-ROM for later recording)
    * `total` (which returns the total playing time of all the tracks added so far)
    * `can_add_track` (which returns a boolean indicating whether there's room
      for a given track)

There are some open ends to this problem. It's suggested that you never add a
track if it cannot fit on the CD-ROM (e.g. the total length will be more than
74 minutes after adding the track). However, whether you decide to do that
with exception handling (discussed later) or by simply doing nothing, is up
to you.

If you finish with that, consider making the number "74" an overridable default
in the class. (That is, make it an attribute in the class, and assign it in the
`__init__` method from a parameter defaulting to 74.)
