from band_basic import *


def main():
    # Test creation
    test_band = BandBasic("The Beatles", "John Lennon")
    print(test_band.info())

    # Test adding of members
    test_band.add_member("Paul McCartney")
    print(test_band.info())

    test_band.add_member("George Harrison")
    print(test_band.info())

    test_band.add_member("Ringo Starr")
    print(test_band.info())

    test_band.add_member("If there are 4 above, this should not be added!")
    print(test_band.info())


main()
