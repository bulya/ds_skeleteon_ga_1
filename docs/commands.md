# ds_skeleteon_ga_1: Commands #

There is multiple commands to run, test, check etc. 
We use `Makefile` to run them, as it is easy to use and understand, 
and it is a standard way to run commands in Unix-like systems.

In `api` directory you can find `Makefile` with all commands related to the `api`. Fill free to add any new 
useful command for you. If you're planing to have client side, you can add `Makefile` to the `client` directory.

On the root directory you can find `Makefile` with all commands related to the project in general. Command with prefix 
`api-` will execute command from `api/Makefile` in docker container with `api` service.
