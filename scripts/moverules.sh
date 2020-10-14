#!/bin/bash -x

# benennt alle .rules Files in .rulesx um oder umgekehrt
# Aufruf via ExecStartPre in systemd-Initfile mit .rules und .rulesx, um rules beim Start zu deaktivieren
# Aufruf via moverules.rules (einzige verbleibende Regel, daher Ignore wichtig !) mit .rulesx und .rules via Timer 5 Minuten nach OH-Start (bzw. Laden von moderules.rules), um rules zu reaktivieren

DIR=/etc/openhab2/rules
ORG=$1
NEW=$2
IGNORE=moverules.rules

echo "==============================================================================" >> /var/log/openhab2/openhab.log
echo "=== Benenne OH-Regeln in $DIR von $1 nach $2 um .... ===" >> /var/log/openhab2/openhab.log
echo "==============================================================================" >> /var/log/openhab2/openhab.log

for f in ${DIR}/*.${ORG};
do
	CURRENT=$(basename $f)
	if [ "$CURRENT" == "$IGNORE" ]; then
		echo "ignoring $IGNORE"
	else
		OLDFILE=$f
		NEWFILE=${f%$ORG}$NEW
		mv "$OLDFILE" "$NEWFILE"
	fi
done
