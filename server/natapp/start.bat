@echo off
path = %~dp0
mkdir tmp 2>NUL
natapp.exe >tmp/stdout.txt