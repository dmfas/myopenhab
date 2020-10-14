"""Logging test"""

from core.rules import rule
from core.triggers import when
from core.log import log_traceback

# pylint: disable=wrong-import-position
import personal.util
reload(personal.util)
from personal.util import SendError, SendWarning, SendInfo, LogInfo, LogDebug


@rule("Log_Test", description="Logtest", tags=["init"])
@when("System started")
@log_traceback
def logtest(event):
    """schreibt testweise verschiedene Logs"""
    msg = str(u"Testausgabe mit äöüß ...")
    # msg = "Testausgabe ohne Sonderzeichen 0: "
    # SendError(msg)
    # SendWarning(msg)
    # SendInfo(msg, logtest.log)
    LogInfo("{}".format(msg), logtest.log)
    # LogDebug("{}".format(msg), logtest.log)
