# SaluteSpeech (STT/TTS) для Home Assistant

Добавляет в HomeAssistant поддержку распознавания речи (STT) и синтеза речи (TTS) через SaluteSpeech Api.

## Установка

- Поместите папку `custom_components/salute_speech` в каталог с кастомными компонентами Home Assistant (/usr/share/hassio/homeassistant).
- Перезапустите Home Assistant.

## Получение ключа для API

1. Откройте сайт smartspeech.sber.ru
2. В разделе `С чего начать`, нажмите `Быстрый старт для физлиц`
3. Следуйте инструкции
4. В разделе `Получите токен доступа` переходим по ссылке `Получаем доступ к API` и выполняем инструкции
5. Из диалога окрывшегося при нажатии `Получить ключ` копируем ключ

## Настройка

1. В интерфейсе Home Assistant откройте `Настройки` → `Устройства и службы` → `Добавить интеграцию` → `SaluteSpeech`.
2. В первое поле вставьте ключ полученный ранее
3. Завершите установку. Теперь в настройках голосового асситента будет достпно распознование и синтез через SaluteSpeech

## Сертификаты

По умолчанию используется цепочка сертификатов МинЦифры поставляемая вместе с компонетом. Если при обращении к API происходят ошибки вида:
```
Error streaming tts: <AioRpcError of RPC that terminated with: status = StatusCode.UNAVAILABLE details = "failed to connect to all addresses; last error: UNKNOWN: ipv4:84.252.144.82:443: Ssl handshake failed (TSI_PROTOCOL_FAILURE): SSL_ERROR_SSL: error:0A000086:SSL routines::certificate verify failed: self-signed certificate in certificate chain"
```

Значит не удалось согласовать соединение с использованием поставляемой цепочки. В таком случае можно указать полный путь к своей цепочке (путь указывается в контексте среды в которой запущен HA).
