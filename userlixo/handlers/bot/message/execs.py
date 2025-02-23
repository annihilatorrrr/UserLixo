# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 Amano Team

import re

from pyrogram import Client, filters
from pyrogram.types import Message

from userlixo.handlers.user.message import cmd, evals, execs


@Client.on_message(
    filters.sudoers & filters.regex(r"^/(?P<command>cmd|sh)\s+(?P<code>.+)", flags=re.S)
)
async def on_cmd_bot(c: Client, m: Message):
    await cmd.cmd(c, m)


@Client.on_message(
    filters.sudoers & filters.regex(r"^/(?P<cmd>ev(al)?)\s+(?P<code>.+)", flags=re.S)
)
async def on_eval_bot(c: Client, m: Message):
    await evals.evals(c, m)


@Client.on_message(
    filters.sudoers & filters.regex(r"^/(?P<cmd>ex(ec)?)\s+(?P<code>.+)", flags=re.S)
)
async def on_exec_bot(c: Client, m: Message):
    await execs.execs(c, m)
