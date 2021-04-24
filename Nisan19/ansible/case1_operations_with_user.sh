# Create Mount Directory If Not Exists
if [[ ! -d /mnt/bootcamp ]]
then
    sudo mkdir -p /mnt/bootcamp
fi

# Mount Disk If It Does Not
if grep -qs '/mnt/bootcamp' /proc/mounts; then
    echo "Disk is mounted"
else    
    /bin/echo -e "n\np\n1\n\n+10G\nw" | sudo fdisk /dev/sdb
    sudo mkfs -t ext4 /dev/sdb1 > ~/memin.txt
    sudo mount /dev/sdb1 /mnt/bootcamp
fi  

# Create opt/bootcamp Directory If Not Exists
if [[ ! -d /opt/bootcamp ]] 
then
    sudo mkdir /opt/bootcamp
    sudo chown root:wheel /opt/bootcamp
    sudo chmod 770 /opt/bootcamp
fi

# Create bootcamp.txt File If Not Exists
if [[ ! -f /opt/bootcamp/bootcamp.txt ]]
then
    sudo echo "merhaba trendyol" >> /opt/bootcamp/bootcamp.txt
fi

# Find The File And Move It.
cd ~/
sudo find / -name bootcamp.txt -exec sudo mv {} /mnt/bootcamp/bootcamp.txt \; 2>/dev/null