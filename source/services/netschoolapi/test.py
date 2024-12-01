import asyncio
from datetime import datetime, timedelta, date
from netschoolapi import NetSchoolAPI
from netschoolapi.errors import AuthError

async def attach_netschoolapi(login, password):
    ns = NetSchoolAPI('https://sgo.edu-74.ru')

    try:
        await ns.login(
            login,
            password,
            'МБОУ "СОШ № 99 г. Челябинска"',
        )
    except AuthError as e:
        return "AuthError"
    except Exception as e:
        return "Error"

    today = date.today()
    day_of_week = today.weekday()

    if day_of_week == 4:  # Пятница
        target_date = today + timedelta(days=3)
    elif day_of_week == 5:  # Суббота
        target_date = today + timedelta(days=2)
    elif day_of_week == 6:  # Воскресенье
        target_date = today + timedelta(days=1)
    else:  # Пн - Чт
        target_date = today + timedelta(days=1)

    bytess = ns.diary()

    bytess = bytess.att

    homework = await ns.download_attachment(attachment_id=334831433)

    await ns.logout()

    return homework

if __name__ == '__main__':
    homework = asyncio.run(attach_netschoolapi("АлексеевР1Р", "999999"))
    print(homework)