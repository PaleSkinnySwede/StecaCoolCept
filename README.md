# StecaCoolCept
Read values from the Steca CoolCept inverter

The Steca CoolCept 3010 is presenting its data in form of an XML file which is accessible in the root of the unit.
Since XML files aren't very pleasing to work with when it comes to finding a specific value from a certain key, I wrote a little Python script to handle it.

The script produces a float() as a result which is the AC_Power readout from the inverter.

# Known issues & To-do
Add code to handle possible disconnects and if the inverter fails to deliver an XML file.
