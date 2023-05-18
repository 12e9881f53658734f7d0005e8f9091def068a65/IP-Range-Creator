b1 = "172"
rangeFile = open("rangefile.txt", "r+")
file = open("file1.txt", "r")

ips = {}

for line in file.readlines():
    ip = line.strip().split(".")
    if ip[1] not in ips:
        ips[ip[1]] = {ip[2]: [1, ip[3]]}
    else:
        if ip[2] not in ips[ip[1]]:
            ips[ip[1]][ip[2]] = [1, ip[3]]
        else:
            ips[ip[1]][ip[2]][0] += 1

for ip1 in ips:
    for ip2 in ips[ip1]:
        count = ips[ip1][ip2][0]
        if count == 1:
            rangeFile.write(f"{b1}.{ip1}.{ip2}.0-{b1}.{ip1}.{ip2}.255 {b1}.{ip1}.{ip2}.{ips[ip1][ip2][1]}\n")
        else:
            rangeFile.write(f"{b1}.{ip1}.{ip2}.0-{b1}.{ip1}.{ip2}.255 {count}\n")

file.close()
rangeFile.close()