import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            ['mpremote', 'connect', "COM4", 'exec', command], #TODO: edit com port number
            stdout=subprocess.PIPE,  # Capture the output of the command
            stderr=subprocess.PIPE,  # Capture any error output
            text=True  # Ensure the output is returned as a string
        )

        # Print the output and error (if any)
        print("Output:")
        print(result.stdout)
        
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    except Exception as e:
        print(f"Error running mpremote: {e}")

def move_wellplate_out():
    """ Moves the wellplate out."""
    command = f"import UV_module; UV_module.move_wellplate_out()"
    run_command(command)

def move_wellplate_in():
    """Moves the moving tray in."""
    command = f"import UV_module; UV_module.move_wellplate_in()"
    run_command(command)

def turn_on_UV(duration): #duration in MINUTES
    """
    Turns on relay for UV lamp for the specified duration of time (in minutes) & turns the lamp off after the duration is complete.

    Parameters:
    ------
    duration (float): time in MINUTES to turn on the UV lamp for.
    """
    command = f"import UV_module; UV_module.turn_on_UV({duration})"
    run_command(command)

# to use module:
# move_wellplate_out()
move_wellplate_in()
turn_on_UV(0.5)
move_wellplate_out()


