import getpass
import os

print("\t\tWelcome to my menu")

passwd = getpass.getpass("Enter the password to continue")
if passwd != 'RedHat':
    exit()

login = input("Where you want to login(local or remote")
while True:
    if login == 'local':
        print(""" We support following option
        1. 	cal command
        2. 	date command
        3. 	df - h command
        4. 	fdisk -l command 
        5. 	To create a physical volume
        6. 	To confirm the Physical volume
        7. 	To craete a volume group
        8. 	To display volume group
        9. 	To create a logical volume 
        10. To display logical volume 
        11. To format the logical volume 
        12. To mount the logical volume
        13. To extend the logical volume size 
        14. To resize the partition
        15. To extend vg
        0. 	To quit
                """)

        ch = int(input("\nEnter your choice : "))
        print(ch)
        if ch == 1:
            os.system("cal")
        elif ch == 2:
            os.system("date")
        elif ch == 3:
            os.system("df -h")
        elif ch == 4:
            os.system("fdisk -l")
        elif ch == 5:
            pv = input("Enter pv name : ")
            os.system("pvcreate {}".format(pv))

        elif ch == 6:
            pv = input("Enter pv name : ")
            os.system("pvdisplay {}".format(pv))

        elif ch == 7:
            vg = input("Enter the volume group name : ")
            os.system("vgcreate {}".format(vg))

        elif ch == 8:
            vg = input("Enter the volume group name : ")
            pv1 = input("Enter the physical volume name : ")
            pv2 = input("Enter the physical volume name : ")
            os.system("vgdisplay {} {} {}".format(vg, pv1, pv2))

        elif ch == 9:
            size = input("Enter the size : ")
            name = input("Enter the name : ")
            vg = input("Enter the vg created : ")
            os.system("lvcreate --size {} --name {} {}".format(size, name, vg))

        elif ch == 10:
            name = input("Enter the LV name(vg/lv)")
            os.system("lvdisplay {}".format(name))

        elif ch == 11:
            name = input(
                """Enter the path of logical volume to format(/dev/vg/lv)""")
            os.system("mkfs.ext4 {}".format(name))

        elif ch == 12:
            mdir = input("Enter the dir name ")
            name = input(
                """Enter the path of logical volume to format(/dev/vg/lv)""")
            os.system("mount {} {}".format(name, mdir))

        elif ch == 13:
            size = input("Enter size to extend eg +5G")
            path = input("ENter the lv path (/dev/vg/lv)")
            os.system("lvextend --size {} {}".format(size, path))

        elif ch == 14:
            name = input("Enter the name for lv to resize(/dev/vg/lv)")
            os.system("resize2fs {}".format(name))

        elif ch == 15:
            name = input("Enter the name of vg")
            hd = input("ENter the name of new hd")

            os.system("vgextend {} {}".format(name, hd))

        elif ch == 0:
            exit()

