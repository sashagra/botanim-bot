from typing import cast

import telegram
from telegram import Update, User
from telegram.ext import ContextTypes

from botanim_bot import config, message_texts
from botanim_bot.services.books import (
    build_category_with_books_string,
    calculate_category_books_start_index,
    get_not_started_books,
)
from botanim_bot.handlers.keyboards import get_categories_keyboard
from botanim_bot.handlers.response import send_response
from botanim_bot.services.validation import is_user_in_channel
from botanim_bot.services.vote_mode import set_user_in_vote_mode
from botanim_bot.services.votings import get_actual_voting


def validate_user(handler):
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = cast(User, update.effective_user).id
        if not is_user_in_channel(user_id, config.TELEGRAM_BOTANIM_CHANNEL_ID):
            await send_response(update, context, message_texts.CANT_VOTE)
            return
        await handler(update, context)

    return wrapped


@validate_user
async def vote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await get_actual_voting() is None:
        await send_response(update, context, message_texts.NO_ACTUAL_VOTING)
        return

    if not update.message:
        return

    categories_with_books = tuple(await get_not_started_books())
    current_category = categories_with_books[0]

    category_books_start_index = calculate_category_books_start_index(
        categories_with_books, current_category
    )

    await set_user_in_vote_mode(cast(User, update.effective_user).id)
    await update.message.reply_text(
        build_category_with_books_string(current_category, category_books_start_index),
        reply_markup=get_categories_keyboard(
            0, len(categories_with_books), config.VOTE_BOOKS_CALLBACK_PATTERN
        ),
        parse_mode=telegram.constants.ParseMode.HTML,
    )
    await send_response(update, context, message_texts.VOTE)


@validate_user
async def vote_button(update: Update, _: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if not query.data or not query.data.strip():
        return
    categories_with_books = list(await get_not_started_books())

    current_category_index = _get_current_category_index(query.data)
    current_category = categories_with_books[current_category_index]

    category_books_start_index = calculate_category_books_start_index(
        categories_with_books, current_category
    )
    await query.edit_message_text(
        text=build_category_with_books_string(
            current_category, category_books_start_index
        ),
        reply_markup=get_categories_keyboard(
            current_category_index,
            len(categories_with_books),
            config.VOTE_BOOKS_CALLBACK_PATTERN,
        ),
        parse_mode=telegram.constants.ParseMode.HTML,
    )


def _get_current_category_index(query_data) -> int:
    pattern_prefix_length = len(config.VOTE_BOOKS_CALLBACK_PATTERN)
    return int(query_data[pattern_prefix_length:])
