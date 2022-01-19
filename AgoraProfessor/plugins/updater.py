import asyncio
import os
import sys
import git
from telethon import events
from AgoraProfessor import AGORA, AGORA2, AGORA3, AGORA4, AGORA5 , AGORA6, AGORA7, AGORA8, AGORA9, AGORA10, AGORA11, AGORA12, AGORA13, AGORA14, AGORA15, AGORA16, AGORA17, AGORA18, AGORA19, AGORA20, AGORA21, AGORA22, AGORA23, AGORA24, AGORA25, AGORA26, AGORA27, AGORA28, AGORA29, AGORA30, AGORA31, AGORA32, AGORA33, AGORA34, AGORA35, AGORA36, AGORA37, AGORA38, AGORA39, AGORA40, DEV, HEROKU_APP_NAME, HEROKU_API_KEY
from .. import CMD_HNDLR as hl

# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/Agora-OS/AGORASPAMGOD"
BOT_IS_UP_TO_DATE = "**AGORA GANGSTERS** is up-to-date sur."
NEW_BOT_UP_DATE_FOUND = (
    "new update found for {branch_name}\n"
    "changelog: \n\n{changelog}\n"
    "updating your AGORO GANGSTERS..."
)
NEW_UP_DATE_FOUND = "New update found for {branch_name}\n" "`updating your AGORA X Spam...`"
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
# -- Constants End -- #

@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in DEV:
        text = "__ updating Your AGORA GANGSTERS __\n **Type** .ping **After 5min To check I'm On !!**"
        await e.reply(text, parse_mode=None, link_preview=None)



@AGORA.on(
    events.NewMessage(pattern="^.update", func=lambda e: e.sender_id in DEV)
)
async def updater(message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(
            IS_SELECTED_DIFFERENT_BRANCH.format(branch_name=active_branch_name)
        )
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = generate_change_log(
        repo,
        DIFF_MARKER.format(
            remote_name=REPO_REMOTE_NAME, branch_name=active_branch_name
        ),
    )

    if not changelog:
        await message.edit("`Updation in Progress......`")
        await asyncio.sleep(5)

    message_one = NEW_BOT_UP_DATE_FOUND.format(
        branch_name=active_branch_name, changelog=changelog
    )
    message_two = NEW_UP_DATE_FOUND.format(branch_name=active_branch_name)

    if len(message_one) > 4095:
        with open("change.log", "w+", encoding="utf8") as out_file:
            out_file.write(str(message_one))
        await AGORA.send_message(
            message.chat_id, document="change.log", caption=message_two
        )
        os.remove("change.log")
    else:
        await message.edit(message_one)

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit(
                        "Invalid APP Name. Please set the name of your bot in heroku in the var `HEROKU_APP_NAME.`"
                    )
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://", "https://api:" + HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(
                    deploy_start(AGORA, message, HEROKU_GIT_REF_SPEC, remote)
                )

            else:
                await message.edit(
                    "Please create the var `HEROKU_APP_NAME` as the key and the name of your bot in heroku as your value."
                )
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("No heroku api key found in `HEROKU_API_KEY` var")


def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    return out_put_str


async def deploy_start(AGORA, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit(
        "__Updated your AGORA GANGSTERS successfully sur__ !!!\n\n"
    )
    await remote.push(refspec=refspec)
    await AGORA.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
