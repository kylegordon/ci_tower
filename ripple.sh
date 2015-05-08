echo 1 > /sys/class/gpio/gpio11/value
sleep 1
echo 0 > /sys/class/gpio/gpio11/value
echo 1 > /sys/class/gpio/gpio12/value
sleep 1
echo 0 > /sys/class/gpio/gpio12/value
echo 1 > /sys/class/gpio/gpio13/value
sleep 1
echo 0 > /sys/class/gpio/gpio13/value
sleep 1

echo 1 > /sys/class/gpio/gpio13/value
sleep 1
echo 0 > /sys/class/gpio/gpio13/value
echo 1 > /sys/class/gpio/gpio12/value
sleep 1
echo 0 > /sys/class/gpio/gpio12/value
echo 1 > /sys/class/gpio/gpio11/value
sleep 1
echo 0 > /sys/class/gpio/gpio11/value

