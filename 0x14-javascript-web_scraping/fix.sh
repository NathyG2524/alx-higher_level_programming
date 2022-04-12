#!/usr/bin/bash

semistandard --verbose | snazzy

semistandard --fix

semistandard --verbose | snazzy

rm *~
