@echo off
set arg1=%1

IF %arg1%==isort (
    isort src/
    )

IF %arg1%==gui (
    python -m src.entrypoints.kivy.main
    )