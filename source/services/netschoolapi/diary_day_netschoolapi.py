import asyncio
from datetime import datetime, timedelta, date
from netschoolapi import NetSchoolAPI
from netschoolapi.errors import AuthError


async def diary_day_netschoolapi(login, password):
    ns = NetSchoolAPI('https://sgo.edu-74.ru')

    try:
        await ns.login(
            login,
            password,
            'МБОУ "СОШ № 99 г. Челябинска"',
        )
    except AuthError:
        return "AuthError"
    except Exception as e:
        print(e)
        return f"Error"

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

    try:
        homework = await ns.diary(start=target_date, end=target_date)
    except Exception as e:
        return f"Error"

    await ns.logout()

    message_text = "<h3><u>Дневник на завтра:</u></h3>\n\n"

    if hasattr(homework, 'schedule') and homework.schedule:
        message_text += f"\n\n<h4>Домашнее задание на {target_date}:</h4>\n\n"
        for day in homework.schedule:
            for lesson in day.lessons:
                assignment_content = 'Нету'
                assignment_comment = 'Нету'
                assignment_mark = 'Нету'

                for assignment in lesson.assignments:
                    assignments_to_show = [
                        assignment for assignment in lesson.assignments
                        if assignment.type == 'Домашнее задание'
                    ]
                    if assignments_to_show:
                        for i, assignment in enumerate(assignments_to_show):
                            assignment_content = assignment.content if assignment.content else "нету"
                            assignment_comment = assignment.comment if assignment.comment else "нету"
                    else:
                        assignment_content = "нету"
                        assignment_comment = "нету"

                    assignment_mark = assignment.mark if assignment.mark else "нету"

                message_text += (
                        f"\n<b><u>{lesson.number}. {lesson.subject}</u></b>\n" +
                        f"• <b>Домашнее задание:</b> <code>{assignment_content}</code>\n" +
                        f"• <b>Комментарий:</b> <code>{assignment_comment}</code>\n" +
                        f"• <b>Оценка:</b> <code>{assignment_mark}</code>" +
                        "\n"
                )

    return message_text

