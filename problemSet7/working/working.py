import re
import sys

# r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$"

def main():
    print(convert(input("Hours: ")))


def convert(s):
    m = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if m:
        ih=int(m.group(1))
        im=m.group(2) if m.group(2) else ':00'
        imeridian=m.group(3)
        fh=int(m.group(4))
        fm=m.group(5) if m.group(5) else ':00'
        fmeridian=m.group(6)

        if imeridian == 'AM':
            ih=0 if ih==12 else ih
        if fmeridian == 'AM':
            fh=0 if fh==12 else fh

        if imeridian == 'PM':
            ih=ih if ih == 12 else ih+12
        if fmeridian == 'PM':
            fh=fh if fh == 12 else fh+12

        return f"{ih:02}{im} to {fh:02}{fm}"
    else:
        raise ValueError()



if __name__ == "__main__":
    main()
