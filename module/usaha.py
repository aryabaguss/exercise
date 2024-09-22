def beban_usaha(operational, non_operational):
    result = operational + non_operational
    return result

def laba_bersih(operational, non_operational, beban):
    result = (operational + non_operational) - beban
    print('Laba bersih yang didapatkan adalah: Rp.{}'.format(result))
