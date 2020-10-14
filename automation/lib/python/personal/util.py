# -*- coding: utf-8 -*-
"""utility methods"""
# pylint: disable=import-error,invalid-name,no-name-in-module
from core.jsr223.scope import actions
from core.log import logging, log_traceback
import configuration
reload(configuration)
from configuration import admin_email, LOG_PREFIX


defaultlog = logging.getLogger("{}.personal.utils".format(LOG_PREFIX))


@log_traceback
def SendAndLogMsg(
        logger,
        level,
        message,
        SendTelegram=False,
        MailSubject=""
    ):
    """Logs messages and eventually notifies user by Telegram and/or mail"""

    loggerfunction = {
        "ERROR": logger.warn,
        "WARN": logger.warn,
        "INFO": logger.info,
        "DEBUG": logger.debug
    }


    out = str(message)
    log = loggerfunction[level]
    log("{}".format(out))

    if SendTelegram:
        t = actions.get("telegram", "telegram:telegramBot:openhab")
        t.sendTelegram(markus_telegram_chatid, out)

    if MailSubject != "":
        actions.get("mail", "mail:smtp:gmx").sendMail(admin_email, MailSubject, message)


# taucht loglevel hiermit am Beginn der Lognachrichten auf? sonst in default parametern hinzufügen
def SendError(message, logger=defaultlog):
    """sends error message to Telegram, sends  mail and prints ERROR level message to openHAB log"""
    SendAndLogMsg(
        logger,
        "ERROR",
        message,
        SendTelegram=True,
        MailSubject="openHAB Fehlermeldung"
    )

def SendWarning(message, logger=defaultlog):
    """sends message to Telegram and prints WARN level message to openHAB log"""
    SendAndLogMsg(
        logger,
        "WARN",
        message,
        SendTelegram=True
    )

def SendInfo(message, logger=defaultlog):
    """sends message to Telegram and prints INFO level message to openHAB log"""
    SendAndLogMsg(
        logger,
        "INFO",
        message,
        SendTelegram=True
    )

def LogInfo(message, logger=defaultlog):
    """prints INFO level message to openHAB log"""
    SendAndLogMsg(
        logger,
        "INFO",
        message
    )


def LogDebug(message, logger=defaultlog):
    """prints DEBUG level message to openHAB log"""
    SendAndLogMsg(
        logger,
        "DEBUG",
        message
    )
