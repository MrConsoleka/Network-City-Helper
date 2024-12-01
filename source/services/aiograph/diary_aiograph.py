import asyncio
from telegraph.aio import Telegraph


async def diary_aiograph(text, member_id):
    try:
        telegraph = Telegraph()
        token = await telegraph.create_account(short_name='sgo_edu_helper_bot')

        html_content = text.replace('\n', '<br>')

        response = await telegraph.create_page(
            f'sgo_edu_helper_bot_{member_id}',
            html_content=html_content,
        )

        response = response['url'].replace("https://telegra.ph/", "")
        return response, token["access_token"]

    except Exception as e:
        return f"Error"