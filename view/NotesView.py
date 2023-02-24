import datetime

from controllers.NotesController import NotesController
from model.Note import Note
from view.NotesCommands import NotesCommands


class NotesView:
    id = 0

    def run(self):
        while True:
            self.greeting()
            inputComand = input('Введите команду: ').upper()
            notesCont = NotesController()
            if inputComand == NotesCommands.EXIT.value:
                exit()

            match inputComand:
                case 'CREATE':
                    topic = input("Введите тему записи:")
                    text = input("Введите текси записи:")
                    date = datetime.date.today()
                    self.id = notesCont.getFinalId()
                    notes = Note(self.id, date, topic, text)
                    notesCont.createNote(notes)
                case 'UPDATE':
                    id = input("Введите номер записи:")

                case 'READ':
                    id = input("Введите номер записи:")
                    notesCont.dataOutput(id)

                case 'LIST':
                    notesCont.dataOutput(None)
                case 'DELETE':
                    notesCont.clearingFile()

    # Пользовательское меню
    def greeting(self):
        print("\nСписок команд записной книги: \n",
              NotesCommands.CREATE.value, "- создание новой записи. \n",
              NotesCommands.READ.value, "- чтение записи по ID. \n",
              NotesCommands.UPDATE.value, "- обновление записи. \n",
              NotesCommands.LIST.value, "- вывод всех записей. \n",
              NotesCommands.DELETE.value, "- удаление записей. \n",
              NotesCommands.EXIT.value, "- выход из программы. \n")
