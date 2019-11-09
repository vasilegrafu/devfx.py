@echo off

SET PATH=i:\Installations\Miniconda3-4.5.4-x86_64\envs\devfx;%PATH%
SET QT_PLUGIN_PATH=i:\Installations\Miniconda3-4.5.4-x86_64\envs\devfx\Library\plugins
SET PYTHONPATH=i:\Dev.Work\devfx.python\solution;%PYTHONPATH%

i:\Installations\VSCode-win32-x64-1.39.1\Code.exe devfx.code-workspace