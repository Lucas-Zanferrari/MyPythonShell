import os


class PythonShellClass:
    def __init__(self):
        """
        This method is the constructor of the class MyPythonShell.
        It is responsible for initialising and updating the three
        attributes current_directory, command and argument (string_input
        is just an auxiliary).
        It also is responsible for the loop that controls the whole
        execution of the program, making decisions of which function
        to call based on the input gave by the user.
        """

        self.current_directory = os.getcwd()    # Gets the path of the current default directory
        print self.current_directory + ' >>>',  # Prints the default directory with three arrows after
        string_input = raw_input()              # Gets the command input from the user

        # Here starts the loop that controls the function calls. It only runs until the user inputs the command quit
        while string_input != "quit":
            try:
                """
                In this block, the program tries to separate the input in two
                strings - command and argument of the command - using a space as the
                delimiter, but sometimes the user may input a string that has no spaces,
                which will cause de program to throw an IndexError exception.
                """
                self.argument = string_input.split(" ", 1)[1]
                self.command = string_input.split()[0]
            except IndexError:
                """
                In this case, the program assigns the following values for command and
                argument. It happens when the user inputs commands as dir, cd without
                arguments, environ etc.)
                """
                [self.command, self.argument] = [string_input, '']

            self.command = self.command.lower()  # Guarantees that the command input will not be case sensitive

            """
            This sequence of if statements is responsible for calling
            the respective appropriate methods according to the user's input,
            passing the argument as a parameter to the method when needed.
            """
            if self.command == "echo":
                self.echo(self.argument)        # Executes the echo method
            elif self.command == "cd":
                self.cd(self.argument)          # Executes the cd method
            elif self.command == "clr":
                self.clr()                      # Executes the clr method
            elif self.command == "environ":
                self.environ()                  # Executes the environ method
            elif self.command == "dir":
                self.dir(self.argument)         # Executes the dir method
            elif self.command == "pause":
                self.pause()                    # Executes the echo method
            elif self.command == "run":
                self.run(self.argument)         # Executes the run method
            elif self.command == "help":
                self.help()                     # Executes the help method
            elif self.command == "top":
                self.top(self.argument)         # Executes the top method
            else:
                print 'Invalid command. Try again.'  # Prints this message if the inserted command is not recognised

            self.current_directory = os.getcwd()    # Updates the current_directory
            print self.current_directory + ' >>>',  # Prints the current_directory
            string_input = raw_input()              # Asks for the next command input

    @staticmethod
    def echo(string_to_print):
        """
        Uses the argument provided to print it in the console screen using the
        native echo command
        """
        os.system("echo " + string_to_print)

    @staticmethod
    def cd(new_directory_path):
        """
        Changes the default directory in which the shell in being executed.
        """
        try:
            # Takes care of removing the possible mistyped spaces the user inserted
            new_directory_path = new_directory_path.replace(" ", "")
            if new_directory_path == '':
                """
                If no new directory path is provided, it changes the default directory to the one
                stored in the environment variable HOME
                """
                os.chdir(os.path.expanduser(os.environ['HOME']))
            else:
                # If a new directory path is provided, it changes the default directory to it.
                os.chdir(os.path.expanduser(new_directory_path))

            os.environ['PWD'] = os.getcwd()  # Update the PWD environment variable
        except OSError:
            """
            If the user inputted a directory path that does not exist, the system
            will throw an exception. The program treats this case by telling the
            user what went wrong and then going back to the control loop, so that
            the user can insert a new path
            """
            print 'Invalid directory path.'

    @staticmethod
    def clr():
        """
        Clears the console screen by executing the correct shell command. The if statement is used to determine
        if the OS is Windows or another, because in Windows' command for clearing the screen is different
        than Linux's and Mac OSX's. They are clear and cls, respectively.
        """
        os.system('clear' if os.name != 'nt' else 'cls')

    @staticmethod
    def environ():
        # Executes the native shell command printenv, which prints all environment variables of the OS and their values
        os.system('printenv')

    @staticmethod
    def dir(path):
        """
        Method designed to print the contents of a folder (located at <path>) on the console.
        """

        # First, it takes care of any mistyped spaces that the user may have inputted by mistake.
        path = path.replace(" ", "")

        if path != '':               # After, it checks if the path is not empty.
            os.system("ls " + path)  # If not, it uses the shell command ls to print the contents in <path>
        else:
            # But if the path is empty, it only displays this error message on the console.
            print 'Directory path cannot be empty.'
        """
        And if the provided path does not exist, MyPythonShell only ignores what the user inputted and
        return to the control loop. It is not necessary to code any error message to be displayed as the
        ls code has one that will be displayed already.
        """

    @staticmethod
    def pause():
        """
        Executes the command read -p with the native shell, which just make the program keep waiting for
        the user to hit [ENTER] on the keyboard. It does that together with printing a instruction for the user.
        """
        os.system("read -p 'Shell is paused. Press [Enter] to return its execution.\n'")

    @staticmethod
    def run(program_path):
        """
        Executes the shell command python <program_path>.
        This will run a python program located at program_path (if there is any).
        It is necessary to have a python compiler installed on the system to make
        this method work.
        """
        os.system('python ' + program_path)

    @staticmethod
    def help():
        """
        Uses the less filter to print a text file called user_manual.txt.
        This text file must be located in the same folder as this shell,
        otherwise the help command will not work properly.
        """
        os.system("less user_manual.txt")

    @staticmethod
    def top(arguments):
        """
        Runs the top program (in the mode defined by the variable arguments) of the OS.
        This program exhibits information regarding the use of the processor.
        """
        os.system("top " + arguments)
