class BandAdvanced:
    def __init__(self, name, firstMember):
        self.band_name = name
        self.members = [firstMember]

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)

    def info(self):
        # Form band information
        band_info = "\nBand Name: " + self.band_name + "\nMembers:\n"

        for member in self.members:
            band_info += (member + "\n")

        return band_info
