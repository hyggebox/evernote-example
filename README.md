# Оставляем заметки в Evernote

Утилита для работы с сервисом Evernote через API

### Установка и запуск

Для работы утилиты необходимы:
- Аккаунт в сервисе Evernote: на время разработки и отладки приложения на 
[sandbox.evernote.com](https://sandbox.evernote.com/Login.action), для конечного приложения на 
[www.evernote.com](https://www.evernote.com/Login.action)
- API-ключ, состоящий из двух значений: **consumer key** и **consumer secret**. 
Получить его можно зарегистрировавшись на [dev.evernote.com](https://dev.evernote.com/#apikey)
- Получить **ключ разработчика** (developer token) на [сайте сервиса](https://www.evernote.com/api/DeveloperToken.action).

Ключи должны быть занесены в файл .env:
```
EVERNOTE_CONSUMER_KEY=<ваш_consumer_key>
EVERNOTE_CONSUMER_SECRET=<ваш_consumer_secret>
EVERNOTE_PERSONAL_TOKEN=<ваш_ключ_разработчика>
```

- На время разработки и отладки приложения в параметрах `EvernoteClient` установить `sandbox=True`, 
для конечного приложения -- `False`:
```python
client = EvernoteClient(
        token=os.environ["EVERNOTE_PERSONAL_TOKEN"],
        sandbox=True
    )
```
- Python2 должен быть установлен. Скачайте из [репозитория](https://github.com/evernote/evernote-sdk-python/) SDK и установите командой:
```shell
python setup.py install
```
- Используйте `pip` для установки зависимостей:

```shell
pip install -r requirements.txt
```

- Запустите нужный скрипт командой `python`. Например:

```shell
python list_notebooks.py
```

## list_notebooks
Скрипт обращается к серверу с использованием персонального ключа разработчика (developer token) и выводит в консоль 
список блокнотов (notebooks) аккаунта: их GUID и заголовки.

## dump_inbox
Выводит список заметок блокнота с указанным GUID в `INBOX_NOTEBOOK_GUID` в файле .env:
```
INBOX_NOTEBOOK_GUID=<GUID_блокнота>
```


По умолчанию выводит в консоль 10 последних заметок. Можно передать любое количество заметок при запуске скрипта:
```
python dump_inbox.py <кол-во_заметок>
```

## add_note2journal

Создаёт копию записи-шаблона с указанным GUID `JOURNAL_TEMPLATE_NOTE_GUID` в блокноте с 
GUID `JOURNAL_NOTEBOOK_GUID` в файле .env:
```
JOURNAL_TEMPLATE_NOTE_GUID=<GUID_заметки-шаблона>
JOURNAL_NOTEBOOK_GUID=<GUID_блокнота>
```
В заголовке шаблона должны быть указаны места вставки даты (*date*) и дня недели (*dow*), например:
"{date} -- {dow}". В заголовок копии по умолчанию вставляется сегодняшняя дата и день недели. При необходимости
можно указать любую другую дату при запуске кода:

```
python add_note2journal.py <дата_в_формате_YYYY-MM-DD>
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).