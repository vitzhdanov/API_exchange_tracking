# exchange_tracking

Путём открытого API отслеживает когда best ask на одной бирже становится меньше, чем best bid
на другой бирже, и оповещает юзера сообщением в телеграм.

С помощью библиотеки "schedule" можно выставить любую переодичность отслеживания(по умолчанию стоит каждые 10мин).

******************************************************************************************************************

Tracks when the best ask on one exchange becomes less than the best bid using an open API
on another exchange, and sends an alert message to the user.

Using the "schedule" library, you can set any frequency of tracking (by default, it is every 10 minutes).
