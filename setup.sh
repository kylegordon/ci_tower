# Export the GPIO pins
echo 11 > /sys/class/gpio/export
echo 12 > /sys/class/gpio/export
echo 13 > /sys/class/gpio/export

# Set their direction
echo out > /sys/class/gpio/gpio11/direction
echo out > /sys/class/gpio/gpio12/direction
echo out > /sys/class/gpio/gpio13/direction
