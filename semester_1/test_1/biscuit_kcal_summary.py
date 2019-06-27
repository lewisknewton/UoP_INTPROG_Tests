def biscuit_slices():
    '''
    Calculate the number of biscuit slices that may be eaten by someone watching their calorie intake.
    '''
    tray_length = float(input('Tray Length (cm): '))
    tray_width = float(input('Tray Width (cm): '))
    num_slices = int(input('Number of Slices: '))

    thickness_of_slice = tray_length / num_slices
    area_of_slice = tray_width * thickness_of_slice

    kcal_plain_slice = int(2 * area_of_slice)
    kcal_choc_topping = 900 // num_slices
    slice_total_kcal = kcal_plain_slice + kcal_choc_topping

    max_slices_allowed = 1000 // slice_total_kcal

    print('\nThickness: ' + str(thickness_of_slice) + ' cm')
    print('Area: ' + str(area_of_slice) + ' cm^2')
    print('Number of calories in each slice: ' + str(slice_total_kcal))
    print('Number of whole slices that may be eaten: ' + str(max_slices_allowed))


biscuit_slices()
