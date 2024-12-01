import asyncio
from datetime import datetime, timedelta, date
from netschoolapi import NetSchoolAPI
from netschoolapi.errors import AuthError


async def diary_tweek_netschoolapi(login, password):
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
        return f"Error: {e}"

    today = date.today()

    if today.weekday() >= 5:
        start_of_week = today + timedelta(days=(7 - today.weekday()))
    else:
        start_of_week = today - timedelta(days=today.weekday())

    monday_t = start_of_week
    tuesday_t = monday_t + timedelta(days=1)
    wednesday_t = monday_t + timedelta(days=2)
    thursday_t = monday_t + timedelta(days=3)
    friday_t = monday_t + timedelta(days=4)

    try:
        monday = await ns.diary(start=monday_t, end=monday_t)
        tuesday = await ns.diary(start=tuesday_t, end=tuesday_t)
        wednesday = await ns.diary(start=wednesday_t, end=wednesday_t)
        thursday = await ns.diary(start=thursday_t, end=thursday_t)
        friday = await ns.diary(start=friday_t, end=friday_t)
    except Exception as e:
        return f"Error fetching: {e}"

    await ns.logout()

    message_text = f"<h3><u>Дневник на недел, с {monday_t} по {friday_t}:</u></h3>\n\n"

    dict_homework_date = [monday_t, tuesday_t, wednesday_t, thursday_t, friday_t]
    dict_homework = [monday, tuesday, wednesday, thursday, friday]

    for homework, homework_date in zip(dict_homework, dict_homework_date):

        if hasattr(homework, 'schedule') and homework.schedule:
            message_text += f"\n\n<h4><u>Домашнее задание на {homework_date}:</u></h4>\n\n"
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
