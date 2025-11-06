class SingletonLogger:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Створення нового екземпляра логгера...")
            cls._instance = super(SingletonLogger, cls).__new__(cls, *args, **kwargs)
            cls._instance.messages = []
        else:
            print("Використання існуючого екземпляра логгера...")
            
        return cls._instance 

    def log(self, message: str):
        self.messages.append(message)
        print(f"[LOG]: {message}")

    def show_logs(self):
        print("\n--- Усі лог-повідомлення ---")
        for msg in self.messages:
            print(f"- {msg}")


logger1 = SingletonLogger()
logger2 = SingletonLogger()
if id(logger1) == id(logger2):
    print("\nlogger1 та logger2 є одним і тим самим об'єктом (id: {})".format(id(logger1)))
else:
    print("\nПомилка! logger1 та logger2 є різними об'єктами.")

print("-" * 30)
logger1.log("Запуск системи...")
logger1.log("Підключення до бази даних...")
print("-" * 30)
logger2.log("Помилка: не вдалося знайти файл 'config.ini'.")
print("-" * 30)
logger1.show_logs()