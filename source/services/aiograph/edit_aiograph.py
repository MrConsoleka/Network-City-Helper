from telegraph import Telegraph
import asyncio


async def edit_aiograph(member_id, text, site, token):
    try:
        telegraph = Telegraph(token)  # чтобы получить доступ к вашим страницам

        html_content = text.replace('\n', '<br>')

        response = telegraph.edit_page(
            path=site,
            title=f"sgo_edu_helper_bot_{member_id}",
            html_content=html_content,
            author_name="",
            author_url="",
            return_content=False
        )

        return response['url']

    except Exception as e:
        return f"Error"
