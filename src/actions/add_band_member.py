from src.models.band import Band, BandMember


def add_band_member(member_name: str, member_instrument: str, band_members_list: list[BandMember]) -> list[BandMember]:
    new_member = BandMember(member_name, member_instrument)
    band_members_list.append(new_member)
    return band_members_list


