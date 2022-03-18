<<<<<<< HEAD
#!/usr/bin/env bash
#Bash script that takes in a URL, sends a request to that URL

curl -sI $1 | grep "Content-Length" | cut -d " " -f2
=======
#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
>>>>>>> 341d78b7e38e2290690928780654d3f27781c2d1
