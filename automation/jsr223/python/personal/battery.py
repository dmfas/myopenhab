"""monitors battery charge state"""
# pylint: disable=import-error,invalid-name,wrong-import-position
from core.rules import rule
from core.triggers import when
from core.metadata import get_key_value
import personal.util
reload(personal.util)
from personal.util import SendWarning, SendInfo, LogInfo
import configuration
reload(configuration)
from configuration import markus_telegram_chatid, LOG_PREFIX
# pylint: enable=import-error,invalid-name,wrong-import-position


@rule("battery monitor", description="check battery percentage", tags=["battery"])
@when("Time cron 0 0 1 * * ?")
#@when("Time cron 0/10 * * * * ?")
def battery_check(event):
    """monitors battery charge state"""
    low_battery_threshold = 20

    def is_battery_low(item, threshold):
        if isinstance(item.state, OnOffType):
            if item.state == "ON":
                LogInfo("{} Batterie Warnung ist ON".format(item.name), battery_check.log)
                return True
        elif isinstance(item.state, DecimalType):
            if item.state < DecimalType(low_battery_threshold):
                SendInfo("{} hat Charge Level {} < {}".format(item.name, item.state, threshold), battery_check.log)
                return True
#        elif isinstance(item.state, UnDefType):
#            SendWarning("{} ist UNDEF".format(item.name), battery_check.log)

        # SendInfo("noch voll, Batterie Charge Level ist {} >= {}".format(item.state, threshold), battery_check.log)
        return False

    battery_low = filter(lambda item: is_battery_low(item, low_battery_threshold), ir.getItem("Batterien").members)
#    if len(battery_low) == 0:
#        SendInfo("Kein Batterieladestand unter der Meldegrenze ({} %)".format(str(low_battery_threshold)), battery_check.log)
#        return

    battery_msg = "Batterieladestand unter der Meldegrenze : {}".format(", ".join(map(lambda sensor: "{}={}".format((get_key_value(sensor.name, "Static", "name") or sensor.name), sensor.state), sorted(sensor for sensor in battery_low))))
    telegram = actions.get("telegram", "telegram:telegramBot:openhab")
#    telegram.sendTelegram(markus_telegram_chatid, battery_msg)
#    log.debug("dir(log)=[{}]".format(dir(log)))
#    SendInfo(battery_msg, battery_check.log)
    SendInfo(battery_msg)

