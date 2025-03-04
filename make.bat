@echo off

SET project_path=src
SET mypylint=mypy %project_path% --ignore-missing-imports --no-warn-unused-ignores --warn-redundant-casts --warn-unused-ignores --pretty --show-error-codes --check-untyped-defs

IF /I "%1"==".DEFAULT_GOAL " GOTO .DEFAULT_GOAL 
IF /I "%1"=="pretty" GOTO pretty
IF /I "%1"=="format" GOTO format
IF /I "%1"=="lint" GOTO lint
IF /I "%1"=="test" GOTO test
GOTO error

:.DEFAULT_GOAL 
	CALL make.bat =
	CALL make.bat all
	GOTO :EOF

:pretty
	ruff format %project_path%
	GOTO :EOF

:format
	ruff format %project_path%
	ruff check --fix
	%mypylint%
	GOTO :EOF

:lint
	ruff check
	%mypylint%
	GOTO :EOF

:test
	pytest %project_path%
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
