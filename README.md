# Загрузка файлов неотъемлемая часть разработки

Бывают случаи когда нужно скачать некоторое количество файлов из сети. Здесь иогут возникнуть следующие проблемы:

+ отсутствие знаний в специализованных для этой задачи библиотеках;

+ недостакок времени.

## Downloader как способ загрузки файлов

Данный модуль позволит вам загружать любые файлы из интерната, также в него встороен другой модуль [**Logger**](https://github.com/LunexCoding/Logger.git), позволяющий наладить логирование вашего приложения.

Логирование здесь объясняется тем, что скорее всего у вас уже есть некое приложение со своей структурой.

Как вы знаете, отладка приложения становится сложнее в зависимости от размера и функционала приложения.

> Сам модуль **Downloader** требует логирования, но если у вас есть логирование для одного модуля, то почему бы не сделать логирование для всего приложения? Вы конечно можете и убрать логирование.

Данный модуль уже имеет первоначальную настройку, а именно:

+ преимущества модуля [**Logger**](https://github.com/LunexCoding/Logger.git);

+ скачанные файлы попадают в созданую модулем папку downloads;


## Использование

Для начала работы нужно выполнить небольшую инструкцию:

1. Склонируйте Logger и Downloader в директорию своего проекта:

    ```
    git clone https://github.com/LunexCoding/Logger
    git clone https://github.com/LunexCoding/Downloader
    ```

    Получится примерная структура:

    ```
    Project
    ├─ Downloader
    │  ├─ README.md
    │  ├─ const.py
    │  └─ downloader.py
    ├─ Logger
    │  ├─ README.md
    │  ├─ __init__.py
    │  └─ log.py
    └─ main.py
    ```

2. Используйте:

    ```python
    # Импорт
    from Downloader import downloadFile
    from Logger import logger

    #Создайте регистратор с указанием именем:
    LOGGER = logger.getLogger(__name__)

    # Используйте объект LOGGER:
    LOGGER.info('start app')

    # Используйте функцию downloadFile
    downloadFile('link', 'filename')

    LOGGER.info('complite app')
    ```

Если возникли вопросы по использованию LOGGER, [смотрите здесь](https://docs.python.org/3/library/logging.html)

---

После запуска кода у вас будет такая структура:

```
Project
├─ Downloader
│  ├─ README.md
│  ├─ __init__.py
│  ├─ const.py
│  └─ downloader.py
├─ Logger
│  ├─ README.md
│  ├─ __init__.py
│  └─ log.py
├─ downloads
│  └─ git.txt
├─ example.py
└─ logs
   └─ app.log
```