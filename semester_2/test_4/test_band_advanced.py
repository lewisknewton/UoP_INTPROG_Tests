from band_advanced import *


def main():
    # Test creation
    test_band = BandAdvanced("Fleetwood Mac", "Mick Fleetwood")
    print(test_band.info())

    # Test adding of members
    test_band.add_member("John McVie")
    print(test_band.info())

    test_band.add_member("Christine McVie")
    print(test_band.info())

    test_band.add_member("Stevie Nicks")
    print(test_band.info())

    test_band.add_member("Stevie Nicks")
    print(test_band.info())


main()
