# pylint: disable=import-error, no-name-in-module

"""Steuerung der Kellerräume"""
from core.rules import rule
from core.triggers import when
# pylint: enable=import-error, no-name-in-module
from personal.util import SendWarning, SendInfo, LogInfo, LogDebug


# da diverse aus dem Core importierte Variablen in pylint verfügbar sind
# pylint: disable=invalid-name, invalid-variable

SchwellwertUntenLuftfeuchteWaschkellerSommerStatisch = 35.0
SchwellwertUntenLuftfeuchteWaschkellerWinterStatisch = 50.0
SchwellwertObenLuftfeuchteWaschkellerStatisch = 65.0
SchwellwertUntenTemperaturWaschkellerStatisch = 10.0
Temp_Kuehlbedarf = 20.0

@rule("Keller Init virtual items", description="Keller items initialisieren", tags=["init"])
@when("Time cron 0 0 1 * * ?")
@when("System started")
def KellerInit(event):
    if items["Schwellwert_unten_Luftfeuchte_Waschkeller"] == NULL:
        events.postUpdate(ir.getItems(SchwellwertUntenLuftfeuchteWaschkeller), SchwellwertUntenLuftfeuchteWaschkellerSommerStatisch
            if now.getMonthOfYear > 3 and now.getMonthOfYear < 10 else SchwellwertUntenLuftfeuchteWaschkellerWinterStatisch)
    if items["Schwellwert_oben_Luftfeuchte_Waschkeller"] == NULL:
        events.postUpdate(SchwellwertObenLuftfeuchteWaschkeller, SchwellwertObenLuftfeuchteWaschkellerStatisch)
    if items["Schwellwert_unten_Temperatur_Waschkeller"] == NULL:
        events.postUpdate(SchwellwertUntenTemperaturWaschkeller, SchwellwertUntenTemperaturWaschkellerStatisch)


@rule("Kellerabgangsraum betreten", description="Kellerabgangsraum betreten")
@when("EG_Kabuff_Auge changed ON")
def Kellerabgangsraum_betreten():
    LogDebug(Kellerabgangsraum_betreten.log,"Kabuff wurde betreten.")

	# EG_Kabuff_Decke.sendCommand(ON)
	# K_Treppe.sendCommand(ON)
	# Kabuff_Nachlauf.sendCommand(ON)
	# Keller_Nachlauf.sendCommand(ON)
