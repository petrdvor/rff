import time
from datetime import datetime


class Rff:
    """Handles the Comsoft recoring file - reads and writes.

    Each rff file starts with 128 bytes header.
    Then, 6 bytes of datablock header follows.
    Then the ASTERIX data block comes.
    Each data block starts with the header.

    | rff file structure:   |
    |-----------------------|
    | 128 bytes file header |
    | 6 bytes block header  |
    | asterix data block    |
    | 6 bytes block header  |
    | asterix data block    |
    | ...                   |

    """

    def __init__(self, file, mode):
        """Initiates the Rff file for reading or writing.

        If mode is 'r' read, the file is open and file header is read.
        Pointer is set to first byte after file header.
        If mode is 'w' write, the file is created and the header is written.

        Parameters:
            file (str): file name
            mode (str): {'r', 'w'} mode of file - either read: 'r' or write 'w'
        """

        self.file = file
        if mode == 'r':
            self.position = 0
            self.header = self._read_header()
        if mode == 'w':
            self._init_rec_file()

    def _read_header(self):
        with open(self.file, "rb") as f:
            f.seek(self.position, 0)
            header = f.read(128)
            self.position += 128
        return header

    def get_header(self):
        """ Provides file header.
        Returns: 
            header (bytes): 128 bits long file header"""
        return self.header

    def get_records(self):
        """Provides ASTERIX records in chunks as denote by the record header
        
        Returns:
            record (bytes): asterix data record
            timestamp (int): number of ms from the recording beginning
        """

        with open(self.file, "rb") as f:
            f.seek(self.position, 0)
            while True:
                astheader = f.read(6)
                if not astheader:
                    break
                self.position += 6
                length = int.from_bytes(astheader[4:6], byteorder='little')

                # time from the beginning of the recording (ms)
                t_stamp = int.from_bytes(astheader[0:4], byteorder='little')

                record = f.read(length)
                self.position += length

                yield record, t_stamp

    def _init_rec_file(self):
        """Initializes the file header when writing to file."""
        # all zeros initialization
        header = bytearray(int('0x00', 16).to_bytes(128, "little"))

        # mandatory bytes
        header[88] = 0x02
        header[89] = 0x03
        header[96] = 0x01
        header[97] = 0x03
        header[121] = 0x0E
        header[126] = 0xA0

        with open(self.file, "wb") as f:
            f.write(header)

        # optional fields
        comment = 'Comment'  # max len=39 bytes
        header_tag = 'RFF    '

        # write time of the recording start
        self.init_time = time.time()

        with open(self.file, "r+") as f:
            f.write(datetime.utcnow().strftime(" %m/%d/%y %H:%M:%S . "))

        # write time of the recording finish
        with open(self.file, "r+") as f:
            f.seek(20, 0)
            f.write(datetime.utcnow().strftime(" %m/%d/%y %H:%M:%S . "))

        # write optional fields
        with open(self.file, "r+") as f:
            f.seek(40, 0)
            f.write(comment[0:39])
            f.seek(80, 0)
            f.write(header_tag)

    def write_record(self, record, *argv):
        """Write header and datablock to file. If timestamp (ms) provided as argv those are used.
            If not provided, calculated function provides.

        Parameters:
            record (bytes): asterix record
            *argv (int): optional, timestamp in ms from the rec. beginning
        """
        stamp = 0
        if argv:
            stamp = argv[0]
        else:
            stamp = int((time.time()-self.init_time)*1000)
        with open(self.file, "ab") as f:
            f.write(stamp.to_bytes(4, byteorder='little'))
            f.write((len(record)).to_bytes(2, byteorder='little'))
            f.write(record)


def main():
    rfile = Rff('./data/sample.rec', 'r')
    wfile = Rff('./data/out.rec', 'w')

    g = rfile.get_records()
    while g:
        try:
            rrr, t_stamp = next(g)
            wfile.write_record(rrr, t_stamp)
            # wfile.write_record(rrr)
        except StopIteration:
            print('End of file.')
            break


if __name__ == "__main__":
    main()
