GREETINGS = """Привееет!

Это Telegram-бот книжного клуба Ботаним.

Здесь можно посмотреть список книг, которые мы читали и планируем читать, \
а также проголосовать за следующую книгу.

Присоединяйся к клубу:
- https://botanim.to.digital — информация о клубе
- https://t.me/+IyGKU9EIGP5jMTky — вход в клуб
- /help — помощь

Команды бота:

/start — приветственное сообщение
/help — справка
/allbooks — все книги, который есть в нашем списке
/already — прочитанные книги
/now — книга, которую сейчас читаем
/vote — проголосовать за следующую книгу
/voteresults — текущие результаты текущего голосования
"""

HELP = """Наш книжный клуб работает по ежемесячной подписке, которая \
стоит 1500 руб/мес. Подписка работает через бот @donate, для того, чтобы \
подписаться, перейди по этой ссылке: https://t.me/+IyGKU9EIGP5jMTky

Ежемесячно мы выбираем здесь голосованием книги и читаем их. По каждой книге \
я (Алексей, автор Диджитализируй) делаю видео и текстовые комментарии, как правило \
по каждой главе, эти материалы попадают в группу в Telegram.

Также мы обсуждаем возникающие по ходу чтения вопросы, сложности и отмечаем \
наиболее полезные части книги, имеющие наибольшее значение для нас.

Присоединяйся!

Если не получается подписаться или есть иные вопросы — пиши на sterx@rl6.ru.
"""

VOTE = """Выше я отправил тебе список книг по всем категориям, которые ты можешь \
листать.

Тебе нужно выбрать три книги из всего списка.

Пришли в ответном сообщении номера книг, которые ты хочешь прочитать. Номера \
можно разделить пробелами, запятыми или переносами строк.

Обрати внимание, что порядок важен — на первом месте книга, которую ты максимально \
хочешь прочесть сейчас.

Например:

53, 8, 102

Победители голосования будут выбраны методом Шульце.

Чтобы выйти из режима голосования, нажми /cancel
"""

VOTE_PROCESS_INCORRECT_INPUT = """Не смог прочесть твоё сообщение.

Напиши три разных номера книги в одном сообщении, наример, так:

53, 8, 102

Чтобы выйти из режима голосования, нажми /cancel
"""

VOTE_PROCESS_INCORRECT_BOOKS = """Переданы некорректные номера книг, пожалуйста,
проверь их.

Нужно передать номера книг из списка выше.
"""

NO_ACTUAL_VOTING = """Сейчас нет активного голосования.

Голосование обычно запускается на ограниченное время на несколько дней.
"""

USER_IN_NOT_VOTE_MODE = """Мой искусственный интеллект пока ещё не слишком интеллект и \
слишком искусственный. Моя твоя не понимать в общем. Давай начнём сначала?

Нажми /start
"""

VOTE_RESULTS_NO_ACTUAL_VOTING = """Сейчас нет активного голосования, поэтому нет и его
результатов:)
"""

SUCCESS_VOTE = """Ура, ты выбрал {books_count}:

{books}

Ты можешь переголосовать до тех пор, пока голосование активно. Для этого просто \
проголосуй повторно с командой
/vote

Посмотреть текущие результаты: /voteresults
"""

SUCCESS_VOTE_BOOK = """{index}. {book.name}"""

VOTE_RESULTS = """<b>ТОП книг голосования</b>

{books}

<i>Даты голосования: с {voting_start} по {voting_finish}
Голосов: {votes_count}</i>

{your_vote}
"""

VOTE_RESULTS_YOUR_VOTE_EXISTS = """<b>Твой выбор</b>

{books}

Переголосовать: /vote"""

VOTE_RESULTS_YOUR_VOTE_NOT_EXISTS = """Ты ещё не проголосовал."""

VOTE_RESULT_BOOK = """{index}. {book}"""
VOTE_RESULT_SEVERAL_BOOKS = "Несколько книг занимают это место:\n    {books}"
VOTE_RESULTS_ZERO_VOTES = "Пока никто не проголосовал, ты можешь стать первым, вжух!"

CANT_VOTE = """Упс, голосование доступно только активным участникам Ботаним!

Подключайтесь: https://t.me/+IyGKU9EIGP5jMTky
"""

ALREADY = """Прочитанные книги:

{books}
"""

ALREADY_BOOK = """{index}. {book_name}\n\
Читали с {book.read_start} по {book.read_finish}, {book.read_comments}\n"""

NOW = """Сейчас мы читаем:

{books}
"""

NOW_BOOK = """{index}{book_name}\n\
Читаем с {book.read_start} по {book.read_finish}, {book.read_comments}"""

BOOK_READ_STARTED = "читаем сейчас"
BOOK_READ_FINISHED = "прочитана"
BOOK_ACTIVE = "— <b>{status}, {read_comments}</b>"
