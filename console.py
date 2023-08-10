import cmd, sys
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        'Quit command to exit the program'
        return (True)
    
    def do_quit(self, line):
        'command to exit the program'
        sys.exit(0)

if __name__ == '__main__':
    HBNBCommand().cmdloop()