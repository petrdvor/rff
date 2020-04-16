# %% COMSOFT rff, POC

# from atm import asterix


def read_file_header(f, position):
    f.seek(position, 0)
    header = f.read(128)
    position += 128
    return position, header


def read_block_header(f, position):
    astheader = f.read(6)
    length = int.from_bytes(astheader[4:6], byteorder='little')
    position += 6
    return position, length


def read_data_block(f, position, length):
    data = f.read(length)
    print(data)

# decoder = asterix.AsterixDecoderPD.AsterixDecoder(10, version='1_1')


# 181 P3D-WS cat20 TP1
with open("data/sample.rec", "rb") as f:

    position = 0

    position, header = read_file_header(f, position)

    position, length = read_block_header(f, position)
    read_data_block(f, position, length)

    # # while length > 0:
    # for i in range(0, 10):
    #     position, length = read_block_header(f, position)
    #     if length == 0:
    #         pass
    #         break
    #     read_data_block(f, position, length)
