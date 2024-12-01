import asyncio
from datetime import datetime, timedelta, date
from netschoolapi import NetSchoolAPI
from netschoolapi.errors import AuthError


async def diary_monthy_netschoolapi(login, password):
    ns = NetSchoolAPI('https://sgo.edu-74.ru')

    try:
        await ns.login(login, password, 'МБОУ "СОШ № 99 г. Челябинска"')
    except AuthError:
        return "AuthError"
    except Exception as e:
        return f"Error: {e}"

    today = date.today()

    # Текущая неделя
    start_of_week = today - timedelta(days=today.weekday())
    monday_t = start_of_week
    tuesday_t = monday_t + timedelta(days=1)
    wednesday_t = monday_t + timedelta(days=2)
    thursday_t = monday_t + timedelta(days=3)
    friday_t = monday_t + timedelta(days=4)

    try:
        monday_cur = await ns.diary(start=monday_t, end=monday_t)
        tuesday_cur = await ns.diary(start=tuesday_t, end=tuesday_t)
        wednesday_cur = await ns.diary(start=wednesday_t, end=wednesday_t)
        thursday_cur = await ns.diary(start=thursday_t, end=thursday_t)
        friday_cur = await ns.diary(start=friday_t, end=friday_t)
    except Exception as e:
        return f"Error fetching current week: {e}"


    # Прошлая неделя
    start_of_last_week = start_of_week - timedelta(days=7)
    monday_last = start_of_last_week
    tuesday_last = monday_last + timedelta(days=1)
    wednesday_last = monday_last + timedelta(days=2)
    thursday_last = monday_last + timedelta(days=3)
    friday_last = monday_last + timedelta(days=4)

    try:
        monday_last_w = await ns.diary(start=monday_last, end=monday_last)
        tuesday_last_w = await ns.diary(start=tuesday_last, end=tuesday_last)
        wednesday_last_w = await ns.diary(start=wednesday_last, end=wednesday_last)
        thursday_last_w = await ns.diary(start=thursday_last, end=thursday_last)
        friday_last_w = await ns.diary(start=friday_last, end=friday_last)
    except Exception as e:
        return f"Error fetching last week: {e}"

    # Следующая неделя
    start_of_next_week = start_of_week + timedelta(days=7)
    monday_next = start_of_next_week
    tuesday_next = monday_next + timedelta(days=1)
    wednesday_next = monday_next + timedelta(days=2)
    thursday_next = monday_next + timedelta(days=3)
    friday_next = monday_next + timedelta(days=4)

    try:
        monday_next_w = await ns.diary(start=monday_next, end=monday_next)
        tuesday_next_w = await ns.diary(start=tuesday_next, end=tuesday_next)
        wednesday_next_w = await ns.diary(start=wednesday_next, end=wednesday_next)
        thursday_next_w = await ns.diary(start=thursday_next, end=thursday_next)
        friday_next_w = await ns.diary(start=friday_next, end=friday_next)
    except Exception as e:
        return f"Error fetching next week: {e}"

    await ns.logout()

    message_text = "<h3><u>Дневник на 3 недели:</u></h3>\n\n"

    def format_homework(homework_list, date_list):
        homework_text = ""
        for homework, homework_date in zip(homework_list, date_list):
            if hasattr(homework, 'schedule') and homework.schedule:
                homework_text += f"\n\n<h4>Домашнее задание на {homework_date}:</h4>\n\n"
                for day in homework.schedule:
                    for lesson in day.lessons:
                        assignment_content = 'Нету'
                        assignment_comment = 'Нету'
                        assignment_mark = 'Нету'
                        for assignment in lesson.assignments:
                            if assignment.type == 'Домашнее задание':
                                assignment_content = assignment.content if assignment.content else "нету"
                                assignment_comment = assignment.comment if assignment.comment else "нету"
                                assignment_mark = assignment.mark if assignment.mark else "нету"
                                break
                        homework_text += (
                            f"\n<b><u>{lesson.number}. {lesson.subject}</u></b>\n" +
                            f"• <b>Домашнее задание:</b> <code>{assignment_content}</code>\n" +
                            f"• <b>Комментарий:</b> <code>{assignment_comment}</code>\n" +
                            f"• <b>Оценка:</b> <code>{assignment_mark}</code>" +
                            "\n"
                        )
        return homework_text

    message_text += f"<h3>Прошлая неделя (с {monday_last} по {friday_last}):</h3>\n"
    message_text += format_homework([monday_last_w, tuesday_last_w, wednesday_last_w, thursday_last_w, friday_last_w], [monday_last, tuesday_last, wednesday_last, thursday_last, friday_last])

    message_text += f"\n<h3>Текущая неделя (с {monday_t} по {friday_t}):</h3>\n"
    message_text += format_homework([monday_cur, tuesday_cur, wednesday_cur, thursday_cur, friday_cur], [monday_t, tuesday_t, wednesday_t, thursday_t, friday_t])

    message_text += f"\n<h3>Следующая неделя (с {monday_next} по {friday_next}):</h3>\n"
    message_text += format_homework([monday_next_w, tuesday_next_w, wednesday_next_w, thursday_next_w, friday_next_w], [monday_next, tuesday_next, wednesday_next, thursday_next, friday_next])

    return message_text
