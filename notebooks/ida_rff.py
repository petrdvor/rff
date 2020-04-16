# %% COMSOFT REC file intial data analysis (rff format)

with open("../data/rec181.rec", "rb") as f:

    position = 0
    f.seek(position, 0)
    header = f.read(128)

    print('                 |Rff file header:')
    print('                 |     bits (len) | content')
    print('                 |----------------|------------')
    print('                 |         0   (1)|', header[0:1])
    print('Start time stamp |    1 -  17 (17)|', header[1:18])
    print('                 |         18  (1)|', header[18:19])
    print('                 |         19  (1)|', header[19:20])
    print('                 |         20  (1)|', header[20:21])
    print('  End time stamp |   21 -  37 (17)|', header[21:38])
    print('                 |         38  (1)|', header[38:39])
    print('                 |         39  (1)|', header[39:40])
    print('         Comment |   40 -  78 (39)|', header[40:79])
    print('                 |         79  (1)|', header[79:80])
    print('                 |   80 -  86  (7)|', header[80:87])
    print('                 |         87  (1)|', header[87:88])
    print('      Header tag |   88 -  89  (2)|', header[88:90])
    print('       Baud rate |   90 -  96  (7)|', header[90:97])
    print('                 |         97  (1)|', header[97:98])
    print('         Padding |   98 - 127 (30)|', header[98:128])

    block_header = f.read(6)
    print('ms from the start time stamp:',
           int.from_bytes(block_header[0:4], byteorder='little'))
    print('length of the asterix block:',
           int.from_bytes(block_header[4:6], byteorder='little'))

    data = f.read(100)
    print(data)

# %%

#181 P3D-WS cat20 TP1
with open("../data/rec181.rec", "rb") as f:
    pass

    position = 0
    f.seek(position, 0)
    header = f.read(128)
 
    print('rec file header:')

    print('      0:', header[0:1])
    print('   1-17:', header[1:18])
    print('     18:', header[18:19])
    print('     19:', header[19:20])
    print('     20:', header[20:21])
    print('  21-37:', header[21:38])
    print('     38:', header[38:39])
    print('     39:', header[39:40])
    print('  40-51:', header[40:51])
    print('  51-52:', header[51:53])
    print('  53-56:', header[53:57])
    print('  57-79:', header[57:80])
    print('  80-82:', header[80:83])
    print('  83-86:', header[83:87])
    print('     87:', header[87:88])
    print('     88:', header[88:89])
    print('     89:', header[89:90])
    print('  90-92:', header[90:93])
    print('  93-95:', header[93:96])
    print('     96:', header[96:97])
    print('     97:', header[97:98])
    print(' 98-104:', header[98:105])
    print('105-113:', header[105:114])
    print('    114:', header[114:115])
    print('115-118:', header[115:119])
    print('119-120:', header[119:121])
    print('    121:', header[121:122])
    print('    122:', header[122:123])
    print('123-125:', header[123:126])
    print('    126:', header[126:127])
    print('    127:', header[127:128])
    print()

