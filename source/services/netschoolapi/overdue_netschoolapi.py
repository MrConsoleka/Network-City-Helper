import asyncio
from netschoolapi import NetSchoolAPI
from netschoolapi.errors import AuthError


async def overdue_netschoolapi(login, password):
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

    overdue = await ns.overdue()

    await ns.logout()

    if len(overdue) > 0:
        message_text = "<b>Ваши просроченные задания:</b>\n"
        for index, assignment in enumerate(overdue, start=1):
            assignment_id = assignment.id if assignment.id else "неизвестно"
            assignment_type = assignment.type if assignment.type else "неизвестно"
            assignment_mark = assignment.mark if assignment.mark else "неизвестно"
            assignment_deadline = assignment.deadline if assignment.deadline else "неизвестно"
            assignment_comment = assignment.comment if assignment.comment else "неизвестно"
            assignment_content = assignment.content if assignment.content else "неизвестно"

            message_text += (f"\n<b>Просроченное задание №{index}:</b>\n\n"
                             f"<b>1. Задание ID:</b>   <code>{assignment_id}</code>\n"
                             f"<b>2. Тип:</b>   <code>{assignment_type}</code>\n"
                             f"<b>3. Оценка:</b>   <code>{assignment_mark}</code>\n"
                             f"<b>4. Срок:</b>   <code>{assignment_deadline}</code>\n"
                             f"<b>5. Комментарий:</b>   <code>{assignment_comment}</code>\n"
                             f"<b>6. Контент:</b>   <code>{assignment_content}</code>\n\n"
                             f"------------------\n")
    else:
        message_text = "Нету просроченных заданий!"

    return message_text