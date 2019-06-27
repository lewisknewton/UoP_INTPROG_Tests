class BandBasic:
    def __init__(self, name, firstMember):
        self.band_name = name
        self.member_1 = firstMember
        self.member_2 = ""
        self.member_3 = ""
        self.member_4 = ""

    def add_member(self, member):
        if self.member_1 == "":
            self.member_1 = member
        elif self.member_2 == "":
            self.member_2 = member
        elif self.member_3 == "":
            self.member_3 = member
        elif self.member_4 == "":
            self.member_4 = member

    def info(self):
        # Form band information
        band_info = ("\nBand Name: {0}"
                     "\nMember1: {1}"
                     "\nMember2: {2}"
                     "\nMember3: {3}"
                     "\nMember4: {4}"
                     ).format(self.band_name,
                              self.member_1,
                              self.member_2,
                              self.member_3,
                              self.member_4)

        return band_info
