# id_app/views.py
from django.shortcuts import render
from .forms import DriverForm
from .qrcode_utils import generate_qr_code

def generate_id_card(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save()  # Save driver details to the database

            # Create a string with all driver data to store in the QR code
            driver_data = f"Name: {driver.name}\nAadhar: {driver.aadhar_card}\nLicense: {driver.driver_license_no}\nTransporter_name: {driver.transporter_name}\nTraining Date: {driver.training_date}\nExpiry Date: {driver.expiry_date}"

            # Generate QR code with driver data
            qr_code_image = generate_qr_code(driver_data)

            # Pass driver data and qr_code_image to the template
            context = {
                'driver': driver,
                'qr_code_image': qr_code_image,  # QR code base64 image
            }

            # Return the rendered template with the driver data and QR code
            return render(request, 'id_card_generator/id_card_template.html', context)

    else:
        form = DriverForm()

    # Render the form for GET requests
    return render(request, 'id_card_generator/driver_form.html', {'form': form})
